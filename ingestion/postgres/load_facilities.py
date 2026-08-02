from ingestion.postgres.postgres_loader import load_postgres_table

load_postgres_table(
    source_table_name = "facilities", 
    target_table_name = "STG_FACILITIES" ,
    target_schema = "STAGING",
    primary_key = "facility_id"
)