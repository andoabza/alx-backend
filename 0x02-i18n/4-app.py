#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""
from flask_babel import Babel, gettext
from flask import Flask, render_template, request


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    query = request.args.get('locale')
    if query in app.config["LANGUAGES"]:
        return query
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('4-index.html', home_title=gettext('home_title'),
                           home_header=gettext('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
