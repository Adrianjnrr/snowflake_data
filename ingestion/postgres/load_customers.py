from ingestion.postgres.postgres_loader import load_postgres_table

load_postgres_table(
    source_table_name = "customers", 
    target_table_name = "STG_CUSTOMERS",
    target_schema = "STAGING",
    primary_key = "customer_id"
)