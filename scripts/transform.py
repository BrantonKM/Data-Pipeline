# scripts/transform.py

import pandas as pd

def transform_airtravel_data(df):
    df.columns = df.columns.str.strip()

    # Melt the year columns into a single 'year' column
    df_melted = df.melt(id_vars=['Month'], var_name='year', value_name='passengers')

    # Normalize values
    df_melted['Month'] = df_melted['Month'].str.strip().str.upper()
    df_melted['year'] = df_melted['year'].astype(str).str.strip()
    df_melted['passengers'] = pd.to_numeric(df_melted['passengers'], errors='coerce')

    # Drop rows with missing passengers
    df_melted.dropna(subset=['passengers'], inplace=True)

    # Save to CSV
    df_melted.to_csv('transformed_airtravel.csv', index=False)
    print("✅ Transformed data saved to transformed_airtravel.csv")

    return df_melted
