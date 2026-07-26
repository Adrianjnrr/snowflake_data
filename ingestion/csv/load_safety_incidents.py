from ingestion.csv.csv_loader import load_csv_table

load_csv_table(
    file_path="data/fleet/safety_incidents.csv",
    target_table_name="STG_SAFETY_INCIDENTS",
    target_schema="STAGING"
)