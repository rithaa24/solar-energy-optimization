from flask import Flask, render_template, url_for, request, jsonify
import os
import pandas as pd
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charts')
def charts():
    return render_template('charts-chartjs.html')

@app.route('/parameters')
def parameters():
    return render_template('maps-google.html')

@app.route('/model_performance')
def model_performance():
    return render_template('pages-blank.html')

@app.route('/data_analysis')
def data_analysis():
    return render_template('pages-profile.html')

@app.route('/references')
def references():
    return render_template('ui-cards.html')

@app.route('/qa')
def qa():
    return render_template('ui-forms.html')

@app.route('/overall_summary')
def overall_summary():
    return render_template('ui-typography.html')

if __name__ == '__main__':
    app.run(debug=True)