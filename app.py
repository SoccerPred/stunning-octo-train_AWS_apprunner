from random import choices
from flask import Flask, request, jsonify
import boto3
import os
import logging
import json
from flask.templating import render_template
import decimal
import streamlit as st

logger = logging.getLogger()
logger.setLevel(logging.INFO)

'''
Defining all variables that need to be retrieved from environment variables
'''
APP_AWS_REGION = os.environ['APP_AWS_REGION'] if "APP_AWS_REGION" in os.environ else "us-east-1"
#APP_DDB_TABLE_NAME = os.environ["APP_DDB_TABLE_NAME"] if "APP_DDB_TABLE_NAME" in os.environ else "apprunner-demo-data"
APP_PORT = os.environ["APP_PORT"] if "APP_PORT" in os.environ else 9090
APP_MODE = os.environ['APP_MODE'] if "APP_MODE" in os.environ else "LOCAL"
APP_DEBUG = True if APP_MODE == "LOCAL" else False


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


app = Flask(__name__, template_folder="html", static_folder="html/static")
app.json_encoder = DecimalEncoder

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/')
def main():
    choices = ['Match Result Prediction','Model Performance']
    ticker = st.sidebar.selectbox('Choose a Page',choices)
    return


@app.route('/api/options')
def get_options():

    return 


@app.route('/api/options')
def vote_option():

    return 

if __name__ == '__main__':
    print("Hello from")
    app.run(port=APP_PORT, host="0.0.0.0", debug=APP_DEBUG)
