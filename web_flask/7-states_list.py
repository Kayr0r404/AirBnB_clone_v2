#!/usr/bin/pythin3
from flask import Flask, render_template
from markupsafe import escape
from models import storage

dict = storage.all('State')

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close_session():
    '''remove the current SQLAlchemy Session'''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)