#!/usr/bin/env python3
"""force locale by passing arg to flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale"""
    local = request.args.get("locale")
    if local and local in app.config["LANGUAGES"]:
        return local
    print(local)
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """index page"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
