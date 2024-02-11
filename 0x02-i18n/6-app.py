#!/usr/bin/env python3
'''user logging system'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


class Config:
    '''config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    '''function to find a user'''
    query = request.args.get('login_as')
    if query:
        user = users.get(int(query))
        return user
    return None


@app.before_request
def before_request() -> None:
    '''function to find a user'''
    user = get_user()
    g.user = user


@babel.localselector
def get_locale() -> str:
    query = g.user['locale']
    if query in app.config('LANGUAGES'):
        return query
    user_setting = g.user['locale']
    if user_setting and user_setting in Config.LANGUAGES:
        return user_setting
    return request.accept_languages.best_match(Config)


@app.route('/')
def hello_world() -> str:
    '''main function'''
    return render_template('5-index.html')


if __name__ == '__main__':
    '''main function'''
    app.run()
