#!/usr/bin/python3
"""Starts a flask app
    listens to 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.teardown_appcontext
def close_session(error):
    '''close the sqlachemy session'''
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def filters():
   # Retrieve and sort cities
    cities = storage.all(City).values()
    cities = sorted(cities, key=lambda k: k.name)

    # Retrieve and sort states
    states = list(storage.all(State).values())
    states = sorted(states, key=lambda k: k.name)

    # Retrieve and sort amenities
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    # Retrieve and sort amenities
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    # Retrieve and sort amenities
    users = storage.all(User).values()
    # users = sorted(users, key=lambda k: k.name)

    return render_template('100-hbnb.html', states=states, cities=cities,
                           amenities=amenities, places=places, users=users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
