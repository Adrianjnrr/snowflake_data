from ingestion.csv.csv_loader import load_csv_table

load_csv_table(
    file_path="data/fleet/drivers.csv",
    target_table_name="STG_DRIVERS",
    target_schema="STAGING"
)