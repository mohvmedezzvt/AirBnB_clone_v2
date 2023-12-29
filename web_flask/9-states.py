#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ display a HTML page """
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='states')


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ display a HTML page """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state, mode='cities')
    return render_template('9-states.html', state=None, mode='none')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
