from postgres_loader import load_postgres_table

load_postgres_table(
    source_table_name = "loads", 
    target_table_name = "STG_LOADS" ,
    target_schema = "STAGING"
)