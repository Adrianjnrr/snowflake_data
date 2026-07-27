from ingestion.csv.csv_loader import load_csv_table
from ingestion.utils.snowflake_connection import get_snowflake_session

session = get_snowflake_session("STAGING")

tables = [
    ("drivers.csv", "STG_DRIVERS"),
    ("trucks.csv", "STG_TRUCKS"),
    ("trailers.csv", "STG_TRAILERS"),
    ("trips.csv", "STG_TRIPS"),
    ("delivery_events.csv", "STG_DELIVERY_EVENTS"),
    ("fuel_purchases.csv", "STG_FUEL_PURCHASES"),
    ("maintenance_records.csv", "STG_MAINTENANCE_RECORDS"),
    ("safety_incidents.csv", "STG_SAFETY_INCIDENTS"),
    ("driver_monthly_metrics.csv", "STG_DRIVER_MONTHLY_METRICS"),
]

for file_name, table_name in tables:
    print(f"Loading {file_name}...")

    try:
        load_csv_table(
            session=session,
            file_path=f"data/fleet/{file_name}",
            target_table_name=table_name,
        )
        print(f"✅ Finished {table_name}")
    except Exception as e:
        print(f"❌ Failed to load {table_name}: {e}")

session.close()    