import duckdb
from ingestion.pipeline import run_pipeline

def test_pipeline_runs():
    run_pipeline()

    conn = duckdb.connect("data/flightpulse.duckdb")

    count = conn.execute("SELECT COUNT(*) FROM raw.flights").fetchone()[0]

    assert count > 0
