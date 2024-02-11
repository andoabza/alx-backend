'''get time zone'''
from flask_babel import Babel
from flask import Flask, render_template, request
from pytz import timezone
from typing import Union, Dict


class Config:
    """Configures the app's available languages.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id.
    """
    login_id = request.args.get('login_as', '')
    if login_id:
        return users.get(int(login_id), None)
    return None


@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution.
    """
    user = get_user()
    g.user = user


@babel.timezoneselector
def get_timezone() -> str:
    """Retrieves the user's timezone.
    """
    try:
        user_timezone = request.args.get('timezone')
        if user_timezone:
            return user_timezone
    except Exception:
        pass
    try:
        if g.user:
            return timezone(g.user['timezone'])
    except Exception:
        pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
