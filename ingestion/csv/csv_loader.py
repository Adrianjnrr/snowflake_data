from requests import session
from snowflake.snowpark import Session
from ingestion.utils.snowflake_connection import get_snowflake_session
from dotenv import load_dotenv
from ingestion.utils.metadata import update_metadata
import uuid
from ingestion.utils.metadata import get_last_processed_key
import pandas as pd



load_dotenv()



def load_csv_table(session, file_path, target_table_name, primary_key):


    # Load CSV into DataFrame
    df = pd.read_csv(file_path, dtype=str).fillna('') 

    last_processed_key = get_last_processed_key(
    session,
    target_table_name
    )

    print(f"Last processed key: {last_processed_key}")

    if last_processed_key:
        df = df[df[primary_key] > last_processed_key]

    print(f"Rows to load: {len(df)}")
    if df.empty:
        print(f"✅ No new records for {target_table_name}")
        return

    print(df.head())
    print(df.shape)

    snowpark_df = session.create_dataframe(df.values.tolist(), schema=df.columns.tolist())

    snowpark_df.write.mode("append").save_as_table(target_table_name)

    if len(df) > 0:
        update_metadata(
        session=session,
        table_name=target_table_name,
        last_processed_key=df[primary_key].max(),
        rows_loaded=len(df),
        status="SUCCESS",
        pipeline_run_id=str(uuid.uuid4())
    )

    
    print(f"✅ {target_table_name} loaded successfully.")

    

