import requests
import pandas as pd

from ingestion.utils.snowflake_connection import get_snowflake_session

# Connect to Snowflake
session = get_snowflake_session("STAGING")

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
        "start_date": "2024-10-29",
        "end_date": "2024-10-30",
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

# Show results
print(weather_df.head())

## Load to Snowflake
snowpark_df = session.create_dataframe(
    weather_df.values.tolist(),
    schema=weather_df.columns.tolist()
)

snowpark_df.write.mode("overwrite").save_as_table(
    "DE_PROJECT.STAGING.STG_WEATHER"
)

print("✅ Weather data loaded successfully!")

session.close()