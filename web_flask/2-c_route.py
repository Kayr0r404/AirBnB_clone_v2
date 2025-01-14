#!/usr/bin/python3
'''script that starts a Flask web application'''

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/ell', strict_slashes=False)
@app.route('/', strict_slashes=False)
def hello():
    '''listening on 0.0.0.0, port 5000'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(escape(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
