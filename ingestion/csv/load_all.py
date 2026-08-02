from ingestion.csv.csv_loader import load_csv_table
from ingestion.utils.snowflake_connection import get_snowflake_session

session = get_snowflake_session("STAGING")

tables = [
    ("drivers.csv", "STG_DRIVERS", "driver_id"),
    ("trucks.csv", "STG_TRUCKS", "truck_id"),
    ("trailers.csv", "STG_TRAILERS", "trailer_id"),
    ("trips.csv", "STG_TRIPS", "trip_id"),
    ("delivery_events.csv", "STG_DELIVERY_EVENTS", "event_id"),
    ("fuel_purchases.csv", "STG_FUEL_PURCHASES", "fuel_purchase_id"),
    ("maintenance_records.csv", "STG_MAINTENANCE_RECORDS", "maintenance_id"),
    ("safety_incidents.csv", "STG_SAFETY_INCIDENTS", "incident_id"),
    ("driver_monthly_metrics.csv", "STG_DRIVER_MONTHLY_METRICS", "driver_id"),
]

for file_name, table_name, primary_key in tables:
    print(f"Loading {file_name}...")

    try:
        load_csv_table(
            session=session,
            file_path=f"data/fleet/{file_name}",
            target_table_name=table_name,
            primary_key=primary_key
        )
        print(f"✅ Finished {table_name}")
    except Exception as e:
        print(f"❌ Failed to load {table_name}: {e}")

session.close()    