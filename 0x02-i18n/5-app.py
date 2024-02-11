'''user logging system'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Dict


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Dict:
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


@app.route('/')
def hello_world() -> str:
    '''main function'''
    return render_template('5-index.html')


if __name__ == '__main__':
    '''main function'''
    app.run()
