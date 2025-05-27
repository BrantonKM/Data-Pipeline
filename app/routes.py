from flask import Flask, render_template
import psycopg2
import pandas as pd
from config.db_config import DB_CONFIG

app = Flask(__name__)

def fetch_data():
    conn = psycopg2.connect(**DB_CONFIG)
    query = "SELECT * FROM airtravel_data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

@app.route('/')
def index():
    df = fetch_data()
    table_data = df.to_html(classes='data', header="true", index=False)
    return render_template("index.html", table=table_data)
