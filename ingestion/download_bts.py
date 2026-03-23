import requests
from pathlib import Path

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

def download_file(url: str, filename: str):
    file_path = DATA_DIR / filename
    
    if file_path.exists():
        print(f"{filename} already exists. Skipping download.")
        return file_path

    print(f"Downloading {filename}...")
    response = requests.get(url)
    response.raise_for_status()

    with open(file_path, "wb") as f:
        f.write(response.content)

    print(f"Saved to {file_path}")
    return file_path


if __name__ == "__main__":
    # Example placeholder — we’ll fix real dataset next
    url = "https://example.com/sample.csv"
    download_file(url, "flights_sample.csv")
