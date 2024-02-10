#!/usr/bin/env python3
'''parametrize templates by _ and gettext'''
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''config babel'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''get locale'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index():
    '''get index'''
    title = gettext('home_title')
    header = gettext('home_header')
    return render_template('3-index.html',
                           main_title=title, main_header=header)


if __name__ == '__main__':
    '''main'''
    app.run()
