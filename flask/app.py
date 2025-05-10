from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return '<html><h1>Hi this is welcome page</h1><html>'


@app.route('/index')
def index():
    return ' this is index pages'


if __name__ == '__main__':
    app.run(debug=True)