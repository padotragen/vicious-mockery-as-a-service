import os
import json
import random
from flask import render_template
from app import app, jsonify

# Define the path to your JSON file
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static/data", "insults.json")

# Load the data at the start of the application
with open(json_url, 'r') as f:
    app_data = json.load(f)

# Define categories for URLs
elements = list(app_data.keys())

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Miguel'}
    return render_template('index.html', title='Home', user=user, categories=elements)

@app.route('/<category>')
def category_insults(category):
    data = app_data[category]
    tit = category
    return render_template('category.html', title=tit, insults=data, categories=elements)
    #return jsonify(data)

@app.route('/<categories>/random')    
def category_insults_random(categories):
    data_len = len(app_data[categories])
    ran_num = random.randint(0, data_len) - 1
    data = app_data[categories][ran_num]
    tit = categories
    return render_template('random.html', title=tit, insult=data, categories=elements)
    #return jsonify(data)

@app.route('/get_insults')
def get_insults():
    return jsonify(app_data)

@app.route('/get_insults/<categories>')
def get_category_insults(categories):
    data = app_data[categories]
    return jsonify(data)

@app.route('/get_insults/<categories>/<int:id>')
def get_category_insults_id(categories,id):
    data = app_data[categories][id]
    return jsonify(data)

@app.route('/get_insults/<categories>/random')
def get_category_insults_random(categories):
    data_len = len(app_data[categories])
    ran_num = random.randint(0, data_len) - 1
    data = app_data[categories][ran_num]
    return jsonify(data)

@app.route('/get_categories')
def get_categories():
    elements = list(app_data.keys())
    return jsonify(elements)