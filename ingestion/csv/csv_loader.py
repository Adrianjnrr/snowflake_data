from dotenv import load_dotenv
from ingestion.utils.metadata import update_metadata, get_last_processed_key
from ingestion.utils.snowflake_connection import get_snowflake_session
import pandas as pd

load_dotenv()


def load_csv_table(
    file_path,
    target_table_name,
    target_schema,
    primary_key,
    pipeline_run_id,
    task_name,
):

    # Create Snowflake session
    session = get_snowflake_session(target_schema)

    # Load CSV
    df = pd.read_csv(file_path, dtype=str).fillna("")

    last_processed_key = get_last_processed_key(
        session=session,
        table_name=target_table_name,
    )

    print(f"Last processed key: {last_processed_key}")

    if last_processed_key:
        df = df[df[primary_key] > last_processed_key]

    print(f"Rows to load: {len(df)}")

    # No new records
    if df.empty:

        update_metadata(
            session=session,
            table_name=target_table_name,
            last_processed_key=last_processed_key,
            rows_loaded=0,
            status="SUCCESS",
            pipeline_run_id=pipeline_run_id,
            task_name=task_name,
        )

        print(f"✅ No new records for {target_table_name}")
        session.close()
        return

    # Load into Snowflake
    snowpark_df = session.create_dataframe(
        df.values.tolist(),
        schema=df.columns.tolist(),
    )

    snowpark_df.write.mode("append").save_as_table(target_table_name)

    update_metadata(
        session=session,
        table_name=target_table_name,
        last_processed_key=df[primary_key].max(),
        rows_loaded=len(df),
        status="SUCCESS",
        pipeline_run_id=pipeline_run_id,
        task_name=task_name,
    )

    print(f"✅ {target_table_name} loaded successfully.")

    session.close()