#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    a function that display Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    a function that display HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def dipslay_text(text):
    """
    Display the value of the variable 'txt' woth underscores replaced
    by spaces
    """
    return f"{text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(
            host='0.0.0.0',
            port=5000,
            debug=True
            )