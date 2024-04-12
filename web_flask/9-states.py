#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Displays an HTML page with a list of states """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<state_id>', strict_slashes=False)
def state_cities(state_id):
    """ Displays an HTML page with a list of cities in a state """
    state = storage.get(State, state_id)
    if state is None:
        return render_template('9-states.html', state=None)
    else:
        return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(exception):
    """ Closes the current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
