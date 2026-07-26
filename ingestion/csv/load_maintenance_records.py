from ingestion.csv.csv_loader import load_csv_table

load_csv_table(
    file_path="data/fleet/maintenance_records.csv",
    target_table_name="STG_MAINTENANCE_RECORDS",
    target_schema="STAGING"
)