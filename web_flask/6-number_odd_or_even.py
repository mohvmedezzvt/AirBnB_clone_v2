#!/usr/bin/python3
""" This module defines a simple Flask application. """
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Route handler for the root URL ("/"). """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Route handler for the URL ("/hbnb"). """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Route handler for the URL ("/c/<text>"). """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """ Route handler for the URL ("/python/<text>"). """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Route handler for the URL ("/number/<n>"). """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Route handler for the URL ("/number_template/<n>"). """
    return render_template("5-number.html", n=n)


@app.route("number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ Route handler for the URL ("/number_odd_or_even/<n>"). """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
