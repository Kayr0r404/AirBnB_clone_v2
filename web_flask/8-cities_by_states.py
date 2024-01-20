from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_session(error):
    '''close the sqlalchemy session'''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    # Retrieve and sort cities
    cities = storage.all(City).values()
    cities = sorted(cities, key=lambda k: k.name)

    # Retrieve and sort states
    states = list(storage.all(State).values())
    states = sorted(states, key=lambda k: k.name)

    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
