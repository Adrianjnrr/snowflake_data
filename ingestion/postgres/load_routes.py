from postgres_loader import load_postgres_table

load_postgres_table(
    source_table_name = "routes", 
    target_table_name = "STG_ROUTES",
    target_schema = "STAGING"
)