from ingestion.csv.csv_loader import load_csv_table

load_csv_table(
    file_path="data/fleet/trailers.csv",
    target_table_name="STG_TRAILERS",
    target_schema="STAGING"
)