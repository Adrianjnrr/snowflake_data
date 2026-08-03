from snowflake.snowpark import Session
from ingestion.utils.snowflake_connection import get_snowflake_session
from sqlalchemy import create_engine
from ingestion.utils.metadata import get_last_processed_key
from dotenv import load_dotenv
from ingestion.utils.metadata import update_metadata

import pandas as pd
import os

load_dotenv()



def load_postgres_table(source_table_name,pipeline_run_id,task_name, target_table_name, target_schema, primary_key):
   
    # PostgreSQL connection
   
    engine = create_engine(
        f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:"
        f"{os.getenv('POSTGRES_PORT')}/"
        f"{os.getenv('POSTGRES_DATABASE')}"
    )

    session = get_snowflake_session(target_schema)

    last_processed_key = get_last_processed_key(
    session=session,
    table_name=target_table_name
    )

    print(f"Last processed key: {last_processed_key}")

    if last_processed_key:
        query = f"""
            SELECT *
            FROM {source_table_name}
            WHERE {primary_key} > '{last_processed_key}'
        """
    else:
        query = f"SELECT * FROM {source_table_name}"

    df = pd.read_sql(query, engine)

    print(df.head())
    print(df.shape)
    
    
    if df.empty:
        update_metadata(
            session=session,
            table_name=target_table_name,
            last_processed_key=last_processed_key,
            rows_loaded=len(df),
            status="SUCCESS",
            pipeline_run_id=pipeline_run_id,
            task_name=task_name
        
        )

        print(f"✅ No new records for {target_table_name}")

        session.close()
        engine.dispose()
        return

   

    
    
    # Load to Snowflake
    database = os.getenv("SNOWFLAKE_DATABASE")
    
    

    snowpark_df = session.create_dataframe(df.values.tolist(),schema=df.columns.tolist())

    snowpark_df.write.mode("append").save_as_table(f"{database}.{target_schema}.{target_table_name}")

    
    print(f"Pipeline Run ID: {pipeline_run_id}")
    print(f"Task Name: {task_name}")

    print("Columns:", df.columns.tolist())
    print("Primary key:", primary_key)
    print("Max key:", df[primary_key].max())

    update_metadata(
    session=session,
    table_name=target_table_name,
    last_processed_key=df[primary_key].max(),
    rows_loaded=len(df),
    status="SUCCESS",
    pipeline_run_id=pipeline_run_id,
    task_name=task_name

)
    print(f"✅ {target_table_name} loaded successfully.")

    session.close()
    engine.dispose()

    
    
   