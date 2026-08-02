from snowflake.snowpark import Session
from datetime import datetime


def get_last_processed_key(session: Session, table_name: str):

    result = session.sql(f"""
        SELECT last_processed_key
        FROM ingestion_metadata
        WHERE table_name = '{table_name}'
        ORDER BY processed_at DESC, pipeline_run_id DESC
        LIMIT 1
    """).collect()

    if result:
        return result[0]["LAST_PROCESSED_KEY"]

    return None



def update_metadata(
    session,
    table_name,
    last_processed_key,
    rows_loaded,
    status,
    pipeline_run_id,
):

    session.sql(f"""
        INSERT INTO ingestion_metadata
        (
            table_name,
            last_processed_key,
            rows_loaded,
            status,
            pipeline_run_id,
            processed_at
        )
        VALUES
        (
            '{table_name}',
            '{last_processed_key}',
            {rows_loaded},
            '{status}',
            '{pipeline_run_id}',
            CURRENT_TIMESTAMP()
        )
    """).collect()