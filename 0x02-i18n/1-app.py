#!/usr/bin/env python3
'''falsk app'''
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    '''config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    '''get home route'''
    return render_template('1-index.html')


if __name__ == '__main__':
    '''main'''
    app.run()
