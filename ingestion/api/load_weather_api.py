import requests
import pandas as pd
from datetime import datetime
import sys
import argparse
from ingestion.utils.metadata import update_metadata
from ingestion.utils.metadata import get_last_processed_key
from ingestion.utils.snowflake_connection import get_snowflake_session

parser = argparse.ArgumentParser()

parser.add_argument("--pipeline-run-id", required=True)
parser.add_argument("--task-name", required=True)

args = parser.parse_args()

START_DATE = "2024-10-29"
END_DATE = "2024-10-30"

# Connect to Snowflake
session = get_snowflake_session("STAGING")

last_processed_key = get_last_processed_key(
    session=session,
    table_name="STG_WEATHER"
)

print(f"Last processed key: {last_processed_key}")

expected_last_timestamp = (
    datetime.strptime(END_DATE, "%Y-%m-%d").strftime("%Y-%m-%d")
    + "T23:00"
)
if last_processed_key == expected_last_timestamp:

    print("✅ Historical weather already loaded.")

    update_metadata(
        session=session,
        table_name="STG_WEATHER",
        last_processed_key=last_processed_key,
        rows_loaded=0,
        status="SUCCESS",
        pipeline_run_id=args.pipeline_run_id,
        task_name=args.task_name,
    )

    session.close()
    sys.exit()

# Read facilities
facilities = session.sql("""
SELECT
    facility_id,
    facility_name,
    city,
    state,
    latitude,
    longitude
FROM STG_FACILITIES
""").to_pandas()

url = "https://archive-api.open-meteo.com/v1/archive"
weather_data = []


for _, row in facilities.iterrows():

    params = {
        "latitude": row["LATITUDE"],
        "longitude": row["LONGITUDE"],
        "start_date": START_DATE,
        "end_date": END_DATE,
        "hourly": [
            "temperature_2m",
            "precipitation",
            "wind_speed_10m",
            "relative_humidity_2m"
        ]
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        hourly = data["hourly"]

        for i in range(len(hourly["time"])):

            weather_data.append({
                "facility_id": row["FACILITY_ID"],
                "facility_name": row["FACILITY_NAME"],
                "city": row["CITY"],
                "state": row["STATE"],
                "latitude": row["LATITUDE"],
                "longitude": row["LONGITUDE"],
                "weather_time": hourly["time"][i],
                "temperature_2m": hourly["temperature_2m"][i],
                "precipitation": hourly["precipitation"][i],
                "wind_speed_10m": hourly["wind_speed_10m"][i],
                "relative_humidity_2m": hourly["relative_humidity_2m"][i]
            })

    else:
        print(f"Failed for {row['FACILITY_NAME']}")

# Convert to DataFrame
weather_df = pd.DataFrame(weather_data)

if weather_df.empty:

    print("❌ No weather data returned from API.")

    session.close()
    sys.exit()

# Show results
print(weather_df.head())

## Load to Snowflake
snowpark_df = session.create_dataframe(
    weather_df.values.tolist(),
    schema=weather_df.columns.tolist()
)

snowpark_df.write.mode("append").save_as_table(
    "DE_PROJECT.STAGING.STG_WEATHER"
)

print("✅ Weather data loaded successfully!")

update_metadata(
    session=session,
    table_name="STG_WEATHER",
    last_processed_key=weather_df["weather_time"].max(),
    rows_loaded=len(weather_df),
    status="SUCCESS",
    pipeline_run_id=args.pipeline_run_id,
    task_name=args.task_name,
)

session.close()