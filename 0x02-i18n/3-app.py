#!/usr/bin/env python3
'''parametrize templates by _ and gettext'''
from flask import Flask, render_template, request
from flask_babel import gettext as _


app = Flask(__name__)


@app.route('/')
def get_index():
    '''get index'''
    return render_template('3-index.html')


if __name__ == '__main__':
    '''main'''
    app.run()
