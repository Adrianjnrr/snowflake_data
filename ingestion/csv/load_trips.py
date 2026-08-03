from ingestion.csv.csv_loader import load_csv_table
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--pipeline-run-id", required=True)
parser.add_argument("--task-name", required=True)

args = parser.parse_args()

load_csv_table(
    file_path="data/fleet/trips.csv",
    target_table_name="STG_TRIPS",
    target_schema="STAGING",
    primary_key="trip_id",
    pipeline_run_id=args.pipeline_run_id,
    task_name=args.task_name
)