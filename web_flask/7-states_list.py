#!/usr/bin/python3
"""Starts a flask app
    listens to 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(error):
    '''close the sqlachemy session'''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = list(storage.all(State).values())
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
