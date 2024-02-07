#!/usr/bin/env python3
'''parametrize templates'''
from flask_babel import Babel, gettext as _
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    '''home route'''
    return render_template('3-index.html')


if __name__ == '__main__':
    '''main'''
    app.run()
