
from flask import jsonify
from server import app
import json
import os


@app.route("/restaurant")
def restaurant():
    """returns restaurant data"""
    base_dir = os.getcwd()
    file_dir = '/server/routes/data/restaurant_data.json'
    file_dir = base_dir + file_dir

    restaurant_data = open (file_dir, "r")
    return json.load(restaurant_data)
    