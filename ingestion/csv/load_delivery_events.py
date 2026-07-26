from ingestion.csv.csv_loader import load_csv_table

load_csv_table(
    file_path="data/fleet/delivery_events.csv",
    target_table_name="STG_DELIVERY_EVENTS",
    target_schema="STAGING"
)