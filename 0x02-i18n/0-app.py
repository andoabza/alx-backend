#!/usr/bin/env python3
"""A Basic Flask app.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    title = 'Welcome to Holberton'
    header = 'Hello world'
    return render_template('0-index.html', title=title, header=header)


if __name__ == '__main__':
    '''main'''
    app.run()
