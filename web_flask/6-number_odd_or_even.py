#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Display "Python" followed by the value
    of the text variable
    """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def python_n(n):
    """
    a function that display "n is a number" only if
    n is an integer
    """
    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """
    A function that display a HTML page only if n is an
    integer
    """
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def odd_or_even(n):
    """
    a function that display htnl page only if n is
    integer
    """
    if isinstance(n, int):
        if n % 2 == 0:
            pair = 'even'
        else:
            pair = 'odd'
        return render_template("6-number_odd_even.html", n=n, pair=pair)

if __name__ == '__main__':
    app.run(
            host='0.0.0.0',
            port=5000,
            debug=True
            )
