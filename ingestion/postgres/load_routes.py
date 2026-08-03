from ingestion.postgres.postgres_loader import load_postgres_table
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--pipeline-run-id", required=True)
parser.add_argument("--task-name", required=True)

args = parser.parse_args()
print(f"Pipeline Run ID: {args.pipeline_run_id}")
print(f"Task Name: {args.task_name}")

load_postgres_table(
    source_table_name = "routes", 
    target_table_name = "STG_ROUTES",
    target_schema = "STAGING",
    primary_key = "route_id",
    pipeline_run_id=args.pipeline_run_id,
    task_name=args.task_name
)