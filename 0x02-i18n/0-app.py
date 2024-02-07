'''falsk app'''
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    '''index route'''
    return render_template('0-index.html')


if __name__ == '__main__':
    '''main'''
    app.run()
