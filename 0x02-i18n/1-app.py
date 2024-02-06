#!/usr/bin/env python3
'''falsk app'''
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)


class Config():
    '''config class'''
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCAL'] = 'en'
app.config['BABEL_DEFAULT_LOCAL_TIMEZONE'] = 'UTC'
babel = Babel(app)


@app.route('/')
def index():
    render_template('1-index.html')
