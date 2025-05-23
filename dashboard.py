import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

# --- DB Config ---
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'Kalekye1222',
    'database': 'data_pipeline'
}

# --- Connect to PostgreSQL ---
@st.cache_data
def load_data():
    engine = create_engine(
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )
    df = pd.read_sql("SELECT * FROM airtravel_data", engine)
    return df

# --- Dashboard UI ---
st.set_page_config(page_title="Air Travel Dashboard", layout="wide")
st.title("📊 Air Travel Data Dashboard")

df = load_data()

# --- Filters ---
st.sidebar.header("Filter Data")
years = st.sidebar.multiselect("Select Year", options=df['Year'].unique(), default=df['Year'].unique())

filtered_df = df[df['Year'].isin(years)]

# --- Show Data ---
st.subheader("✈️ Filtered Data")
st.dataframe(filtered_df)

# --- Summary Stats ---
st.subheader("📈 Summary")
st.metric("Total Passengers", f"{filtered_df['Total'].sum():,}")
