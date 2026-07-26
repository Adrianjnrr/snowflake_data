from snowflake.snowpark import Session
from ingestion.utils.snowflake_connection import get_snowflake_session
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()



def load_csv_table(session, file_path, target_table_name):
    # Load CSV into DataFrame
    df = pd.read_csv(file_path, dtype=str).fillna('')  

    print(df.head())
    print(df.shape)

    snowpark_df = session.create_dataframe(df.values.tolist(), schema=df.columns.tolist())

    snowpark_df.write.mode("overwrite").save_as_table(target_table_name)
    print(f"✅ {target_table_name} loaded successfully.")

    

