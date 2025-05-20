# scripts/extract.py

import requests
import os

def download_csv(url, save_path):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"[✓] File downloaded to: {save_path}")
    else:
        print(f"[✗] Failed to download file. Status code: {response.status_code}")

# Quick test
if __name__ == "__main__":
    test_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    os.makedirs("data", exist_ok=True)
    download_csv(test_url, "data/raw_data.csv")