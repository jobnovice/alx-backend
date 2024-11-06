#!/usr/bin/env python3
"""1-app.py"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """wrote a class that configures the flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """defines the route the landing page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)