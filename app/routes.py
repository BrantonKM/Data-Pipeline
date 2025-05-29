
from flask import Blueprint, render_template, send_file, request
import pandas as pd
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    df = pd.read_csv('data/transformed_airtravel.csv')
    years = sorted(df['year'].unique())
    months = sorted(df['Month'].unique())
    selected_year = request.args.get('year', '')
    selected_month = request.args.get('Month', '')

    filtered_df = df.copy()
    if selected_year:
        filtered_df = filtered_df[filtered_df['year'] == int(selected_year)]
    if selected_month:
        filtered_df = filtered_df[filtered_df['Month'] == selected_month]

    labels = filtered_df['Month'].tolist()
    values = filtered_df['passengers'].tolist()

    return render_template('index.html', data=filtered_df.to_dict(orient='records'),
                           years=years, months=months, selected_year=selected_year,
                           selected_month=selected_month, labels=labels, values=values)

@main.route('/forecast')
def forecast():
    df = pd.read_csv('data/transformed_airtravel.csv')
    df['passengers'] = pd.to_numeric(df['passengers'], errors='coerce')
    df.dropna(subset=['passengers'], inplace=True)
    df['forecast'] = df['passengers'].rolling(window=3).mean()
    labels = df['Month'].tolist()
    actual = df['passengers'].tolist()
    predicted = df['forecast'].tolist()
    return render_template('forecast.html', labels=labels, actual=actual, predicted=predicted)

@main.route('/download')
def download():
    file_path = os.path.join('data', 'transformed_airtravel.csv')
    return send_file(file_path, as_attachment=True)
