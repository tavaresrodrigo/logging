import logging
import json
import random
import csv
import logging.handlers
import json
import subprocess
import time
from flask import Flask, jsonify, render_template, Response
from piadas import log_entries
from collections import OrderedDict

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

#iterate the jokes dictionary and log json log format to stdout for each 200 request
@app.route('/json')
def json_log():
    for log_entry in log_entries:
        app.logger.info(json.dumps(log_entry))
    return jsonify(log_entries)


# #iterate the jokes dictionary and log csv log format to stdout for each 200 request
# @app.route('/csv')
# def csv():


# #iterate the jokes dictionary and log appache log format to stdout for each 200 request
# @app.route('/apacche')
# def apache():

     
# #iterate the jokes dictionary and log nginx log format to stdout for each 200 request
# @app.route('/nginx')
# def nginx():

   
# #iterate the jokes dictionary and log syslog log format to stdout for each 200 request
# @app.route('/syslog')
# def syslog():


# #iterate the jokes dictionary and log dmesg log format to stdout for each 200 request
# @app.route('/dmesg')
# def dmesg():
     
if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)
    app.run(debug=True, host='0.0.0.0')