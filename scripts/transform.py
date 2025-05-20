# scripts/transform.py

import pandas as pd

def clean_data(input_path):
    try:
        df = pd.read_csv(input_path)
        print(f"[✓] Raw data loaded. Shape: {df.shape}")
    except Exception as e:
        print(f"[✗] Error reading CSV: {e}")
        return None

    # Clean column names
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    
    # Drop rows with missing values
    df = df.dropna()

    print(f"[✓] Data cleaned. Final shape: {df.shape}")
    return df

# Quick test
if __name__ == "__main__":
    clean_df = clean_data("data/raw_data.csv")
    print(clean_df.head())