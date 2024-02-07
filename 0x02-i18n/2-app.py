#!/usr/bin/env python3
'''get locale'''
from flask import request, Flask, render_template
from flask_babel import Babel, babel


app = Flask(__name__)
app.url_map.strict_slashes = False
babel.init_app(app)


@babel.localeselector
def get_locale():
    '''get local language and time'''
    return request.accept_languages.best_match(app.config('LANGUAGES'))


@app.route('/')
def index() -> str:
    '''home route'''
    return render_template('2-index.html')


if __name__ == '__main__':
    '''main'''
    app.run()
