
'''parametrize templates by _ and gettext'''
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
import babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def get_index():
    '''get index'''
    title = gettext('home_title')
    header = gettext('home_header')
    return render_template('3-index.html', main_title=title, main_header=header)


if __name__ == '__main__':
    '''main'''
    app.run()
