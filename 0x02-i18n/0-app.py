#!/usr/bin/env python3
'''falsk app'''
from flask import render_template
app = flask(__name__)


@app.route('/')
def index():
    return render_template('0-index.html')
