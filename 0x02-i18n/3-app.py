#!/usr/bin/env python3
'''parametrize templates by _ and gettext'''
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''config babel'''
    LANGUAGES = ['en', 'es']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def get_index():
    '''get index'''
    return render_template('3-index.html')


if __name__ == '__main__':
    '''main'''
    app.run()
