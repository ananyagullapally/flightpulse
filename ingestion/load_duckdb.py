import duckdb
import pandas as pd
from pathlib import Path

# Paths
DB_PATH = "data/flightpulse.duckdb"
DATA_FILE = Path("data/raw/routes.dat")


def load_csv_to_duckdb():
    # Check file exists
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"{DATA_FILE} not found. Run ingestion first.")

    print("Loading data into DuckDB...")

    # Connect to DB
    conn = duckdb.connect(DB_PATH)

    # Read CSV (no headers in OpenFlights dataset)
    df = pd.read_csv(DATA_FILE, header=None)

    # Assign column names (CRITICAL FIX)
    df.columns = [
        "airline",
        "airline_id",
        "source_airport",
        "source_airport_id",
        "destination_airport",
        "destination_airport_id",
        "codeshare",
        "stops",
        "equipment"
    ]

    # Create schema
    conn.execute("CREATE SCHEMA IF NOT EXISTS raw")

    # Drop table if exists (idempotent pipeline)
    conn.execute("DROP TABLE IF EXISTS raw.flights")

    # Register dataframe as temporary view
    conn.register("df_view", df)

    # Create table from dataframe
    conn.execute("""
        CREATE TABLE raw.flights AS
        SELECT * FROM df_view
    """)

    # Basic sanity check
    count = conn.execute("SELECT COUNT(*) FROM raw.flights").fetchone()[0]
    print(f"Loaded {count} rows into raw.flights")

    conn.close()


if __name__ == "__main__":
    load_csv_to_duckdb()
