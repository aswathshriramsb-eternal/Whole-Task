"""
app.py
Flask Backend for Project 02: Data Visualization with Matplotlib & Seaborn
Serves the interactive web dashboard and provides REST API endpoints for
dataset records, statistical summaries, and dynamic filtering.
"""

import os
import json
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request, send_from_directory, render_template

# Initialize Flask application
app = Flask(__name__, static_folder='.', static_url_path='')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'tips.csv')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')

# Load the authentic Seaborn tips dataset
if os.path.exists(DATA_FILE):
    df_global = pd.read_csv(DATA_FILE)
else:
    # Fallback to seaborn if file not found
    import seaborn as sns
    df_global = sns.load_dataset('tips')
    os.makedirs(os.path.join(BASE_DIR, 'data'), exist_ok=True)
    df_global.to_csv(DATA_FILE, index=False)

# Add derived columns
df_global['tip_pct'] = (df_global['tip'] / df_global['total_bill'] * 100).round(2)


@app.route('/')
def index():
    """Serve the primary dashboard interface."""
    return send_from_directory(BASE_DIR, 'index.html')


@app.route('/api/data', methods=['GET'])
def get_data():
    """
    Return dataset records with optional filtering:
    - day: Thur, Fri, Sat, Sun
    - time: Lunch, Dinner
    - smoker: Yes, No
    """
    df_filtered = df_global.copy()

    day = request.args.get('day')
    time = request.args.get('time')
    smoker = request.args.get('smoker')

    if day and day.lower() != 'all':
        df_filtered = df_filtered[df_filtered['day'].str.lower() == day.lower()]
    if time and time.lower() != 'all':
        df_filtered = df_filtered[df_filtered['time'].str.lower() == time.lower()]
    if smoker and smoker.lower() != 'all':
        df_filtered = df_filtered[df_filtered['smoker'].str.lower() == smoker.lower()]

    records = df_filtered.to_dict(orient='records')
    return jsonify({
        'status': 'success',
        'count': len(records),
        'total_unfiltered': len(df_global),
        'data': records
    })


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """
    Compute and return dynamic statistical metrics and correlation matrix.
    Supports query filters to recalculate metrics dynamically.
    """
    df_filtered = df_global.copy()

    day = request.args.get('day')
    time = request.args.get('time')
    smoker = request.args.get('smoker')

    if day and day.lower() != 'all':
        df_filtered = df_filtered[df_filtered['day'].str.lower() == day.lower()]
    if time and time.lower() != 'all':
        df_filtered = df_filtered[df_filtered['time'].str.lower() == time.lower()]
    if smoker and smoker.lower() != 'all':
        df_filtered = df_filtered[df_filtered['smoker'].str.lower() == smoker.lower()]

    if len(df_filtered) == 0:
        return jsonify({
            'status': 'error',
            'message': 'No records match the selected criteria.'
        }), 404

    # Day breakdown
    day_stats = df_filtered.groupby('day', observed=False).agg(
        avg_tip=('tip', 'mean'),
        avg_bill=('total_bill', 'mean'),
        count=('tip', 'count')
    ).round(2).reset_index().to_dict(orient='records')

    # Meal time breakdown
    time_stats = df_filtered.groupby('time', observed=False).agg(
        avg_tip=('tip', 'mean'),
        avg_bill=('total_bill', 'mean'),
        count=('tip', 'count')
    ).round(2).reset_index().to_dict(orient='records')

    # Correlation matrix for numerical fields
    num_cols = ['total_bill', 'tip', 'size']
    corr = df_filtered[num_cols].corr().round(4).to_dict()

    stats = {
        'total_records': int(len(df_filtered)),
        'total_unfiltered': int(len(df_global)),
        'num_numerical_features': 3,
        'num_categorical_features': 4,
        'avg_bill': round(float(df_filtered['total_bill'].mean()), 2),
        'median_bill': round(float(df_filtered['total_bill'].median()), 2),
        'min_bill': round(float(df_filtered['total_bill'].min()), 2),
        'max_bill': round(float(df_filtered['total_bill'].max()), 2),
        'avg_tip': round(float(df_filtered['tip'].mean()), 2),
        'median_tip': round(float(df_filtered['tip'].median()), 2),
        'min_tip': round(float(df_filtered['tip'].min()), 2),
        'max_tip': round(float(df_filtered['tip'].max()), 2),
        'avg_size': round(float(df_filtered['size'].mean()), 2),
        'avg_tip_pct': round(float(df_filtered['tip_pct'].mean()), 2),
        'day_breakdown': day_stats,
        'time_breakdown': time_stats,
        'correlations': corr,
        'highest_tip_day': max(day_stats, key=lambda x: x['avg_tip'])['day'] if day_stats else None
    }

    return jsonify({
        'status': 'success',
        'stats': stats
    })


@app.route('/outputs/<path:filename>')
def serve_output(filename):
    """Serve generated Matplotlib and Seaborn visualization images."""
    return send_from_directory(OUTPUT_DIR, filename)


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'dataset_loaded': True,
        'records': len(df_global)
    })


if __name__ == '__main__':
    print("==================================================================")
    print(" PROJECT 02: DATA VISUALIZATION WITH MATPLOTLIB & SEABORN")
    print(" Starting Flask Web Application at: http://127.0.0.1:5000")
    print(" Press Ctrl+C in terminal to stop.")
    print("==================================================================")
    app.run(host='127.0.0.1', port=5000, debug=True)
