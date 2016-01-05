import sys
import os
from flask.ext.cors import CORS
from flask import Flask, request, make_response, session, g, redirect, url_for, \
     abort, render_template, flash ,session, Response
import json
import flask
from job_handlers.jobManager import JobManager

# Set parameters
debugFlag = False  # Should be false for prod
runLocal = False  # False for prod, when True this assumes that the Dynamo is on the same server
createTable = False  # Should be false for most runs, true for first run with DynamoDB

# Get the project's root folder
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Create application
app = Flask(__name__)
app.config.from_object(__name__)

cors = CORS(app)

# Root will point to index.html
@app.route("/", methods=["GET"])
def root():
    return "Job manager is running"

# Job manager routes
@app.route("/startJobs/", methods=["POST"])
def start_jobs():
    JobManager().startReady()

if __name__ == '__main__':
    app.run(debug=debugFlag,threaded=True,host="0.0.0.0")
