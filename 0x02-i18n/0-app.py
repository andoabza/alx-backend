#!/usr/bin/env python3
'''falsk app'''
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('0-index.html')