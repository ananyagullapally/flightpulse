from ingestion.download_bts import download_file
from ingestion.load_duckdb import load_csv_to_duckdb


def run_pipeline():
    url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat"
    
    # IMPORTANT: filename must match loader
    download_file(url, "routes.dat")

    load_csv_to_duckdb()


if __name__ == "__main__":
    run_pipeline()
