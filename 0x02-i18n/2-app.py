#!/usr/bin/env python3
'''get locale'''
from flask import request, Flask
from flask_babel import Babel


def get_locale():
    '''get local language and time'''
    return request.accept_languages.best_match(app.config('LANGUAGES'))


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)
