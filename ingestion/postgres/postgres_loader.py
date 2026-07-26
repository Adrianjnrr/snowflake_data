from snowflake.snowpark import Session
from ingestion.utils.snowflake_connection import get_snowflake_session
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()


mfa_code = input("Enter your 6-digit MFA code: ")

def load_postgres_table(source_table_name, target_table_name, target_schema):
   
    # PostgreSQL connection
   
    engine = create_engine(
        f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:"
        f"{os.getenv('POSTGRES_PORT')}/"
        f"{os.getenv('POSTGRES_DATABASE')}"
    )

    query = f"SELECT * FROM {source_table_name}"

    df = pd.read_sql(query, engine)

    print(df.head())
    print(df.shape)

   
    # Snowflake connection
    session = get_snowflake_session()
    
    
    # Load to Snowflake
    database = os.getenv("SNOWFLAKE_DATABASE")
    
    

    snowpark_df = session.create_dataframe(df.values.tolist(),schema=df.columns.tolist())

    snowpark_df.write.mode("overwrite").save_as_table(f"{database}.{target_schema}.{target_table_name}")
    print(f"✅ {target_table_name} loaded successfully.")

    session.close()
    engine.dispose()

    
    
   