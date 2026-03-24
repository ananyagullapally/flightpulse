from prefect import flow, task
import subprocess


@task(retries=2, retry_delay_seconds=10)
def run_ingestion():
    subprocess.run(["python", "-m", "ingestion.pipeline"], check=True)


@task
def run_dbt():
    subprocess.run(["dbt", "run"], cwd="flightpulse_dbt", check=True)


@task
def test_dbt():
    subprocess.run(["dbt", "test"], cwd="flightpulse_dbt", check=True)


@flow(name="flightpulse-pipeline")
def pipeline():
    run_ingestion()
    run_dbt()
    test_dbt()


if __name__ == "__main__":
    pipeline()
