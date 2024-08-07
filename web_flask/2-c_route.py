#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
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
    Display "C" followed by the value of the
    variable 'txt' woth underscores replaced
    by spaces
    """
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == '__main__':
    app.run(
            host='0.0.0.0',
            port=5000,
            debug=True
            )
