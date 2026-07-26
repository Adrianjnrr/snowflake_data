from ingestion.csv.csv_loader import load_csv_table

load_csv_table(
    file_path="data/fleet/driver_monthly_metrics.csv",
    target_table_name="STG_DRIVER_MONTHLY_METRICS",
    target_schema="STAGING"
)