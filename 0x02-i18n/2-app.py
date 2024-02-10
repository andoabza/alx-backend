'''get locale with @babel.localeselector'''

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    '''config class'''
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    '''get locale'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''home route'''
    return render_template('2-index.html')


if __name__ == '__main__':
    '''main'''
    app.run()
