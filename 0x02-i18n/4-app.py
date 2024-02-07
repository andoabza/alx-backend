'''get locale'''
from flask import request, Flask, render_template
from flask_babel import babel


app = Flask(__name__)
app.url_map.strict_slashes = False
babel.init_app(app)


@babel.localeselector
def get_locale() -> str:
    '''get local language and time'''
    local = request.args.get('locale')
    support = ['en', 'fr']
    if local in support:
        return local
    return ['en']

@app.route('/')
def index() -> str:
    '''home route'''
    return render_template('4-index.html')


if __name__ == '__main__':
    '''main'''
    app.run()
