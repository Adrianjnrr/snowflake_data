from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

PROJECT_DIR = "/Users/joseph/Desktop/snowflake-data-platform"
PYTHON = f"{PROJECT_DIR}/.venv-1/bin/python"

POSTGRES_TASKS = [
    "load_customers",
    "load_facilities",
    "load_routes",
    "load_loads",
]

CSV_TASKS = [
    "load_driver",
    "load_trucks",
    "load_trailers",
    "load_trips",
    "load_delivery_events",
    "load_fuel_purchase",
    "load_maintenance_records",
    "load_safety_incidents",
    "load_driver_monthly_metrics",
]

with DAG(
    dag_id="fleet_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule="@daily",
    catchup=False,
    tags=["portfolio"],
) as dag:

    postgres_tasks = {}
    csv_tasks = {}

    
    for task in POSTGRES_TASKS:

        postgres_tasks[task] = BashOperator(
            task_id=task,
            cwd=PROJECT_DIR,
            bash_command=f"""
            {PYTHON} -m ingestion.postgres.{task} \
            --pipeline-run-id "{{{{ run_id }}}}" \
            --task-name "{task}"
            """,
        )

    
    for task in CSV_TASKS:

        csv_tasks[task] = BashOperator(
            task_id=task,
            cwd=PROJECT_DIR,
            bash_command=f"""
            {PYTHON} -m ingestion.csv.{task} \
            --pipeline-run-id "{{{{ run_id }}}}" \
            --task-name "{task}"
            """,
        )

    weather_task = BashOperator(
    task_id="load_weather_api",
    cwd=PROJECT_DIR,
    bash_command=f"""
    {PYTHON} -m ingestion.api.load_weather_api \
    --pipeline-run-id "{{{{ run_id }}}}" \
    --task-name "load_weather_api"
    """,
    )

    
    for postgres_task in postgres_tasks.values():

        for csv_task in csv_tasks.values():
            postgres_task >> csv_task

    for csv_task in csv_tasks.values():
        csv_task >> weather_task        