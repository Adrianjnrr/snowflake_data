from ingestion.csv.csv_loader import load_csv_table

load_csv_table(
    file_path="data/fleet/fuel_purchases.csv",
    target_table_name="STG_FUEL_PURCHASES",
    target_schema="STAGING"
)