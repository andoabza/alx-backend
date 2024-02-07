#!/usr/bin/env python3
'''falsk app'''
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.url_map.strict_slashes = False


class Config():
    '''config class'''
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)


@app.route('/')
def get_index():
    '''get home route'''
    return render_template('1-index.html')


if __name__ == '__main__':
    '''main'''
    app.run()
