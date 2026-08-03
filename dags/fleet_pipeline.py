from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

PROJECT_DIR = "/Users/joseph/Desktop/snowflake-data-platform"
PYTHON = f"{PROJECT_DIR}/.venv-1/bin/python"

with DAG(
    dag_id="fleet_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule="@daily",
    catchup=False,
    tags=["portfolio"],) as dag:

    load_customers = BashOperator(
        task_id="load_customers",
        cwd = PROJECT_DIR,
        bash_command = f"{PYTHON} -m ingestion.postgres.load_customers"
    )

