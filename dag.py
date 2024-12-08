from dagster import DagsterInstance, RunsFilter, DagsterRunStatus

# Get the Dagster instance
instance = DagsterInstance.get()

# Query the most recent successful run
run_records = instance.get_run_records(
    filters=RunsFilter(statuses=[DagsterRunStatus.SUCCESS]),
    limit=1
)

# Ensure there is at least one run record
if run_records:
    recent_run = run_records[0].dagster_run
    run_id = recent_run.run_id
    run_config = recent_run.run_config

    print(f"Run ID: {run_id}")
    print(f"Run Config: {run_config}")
##################################################
from dagster import DagsterInstance, RunsFilter, PipelineRunStatus

# Get the Dagster instance
instance = DagsterInstance.get()

# Fetch the most recent successful run for a specific job
run_records = instance.get_run_records(
    filters=RunsFilter(job_name="your_job_name", statuses=[PipelineRunStatus.SUCCESS]),
    limit=1
)

# Check if any runs were found
if run_records:
    # Get the run configuration of the most recent run
    recent_run = run_records[0].dagster_run
    run_config = recent_run.run_config
    print("Run Config:", run_config)
else:
    print("No recent runs found.")

