#!/usr/bin/env python3
"""3-app.py defined"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """class to configure the flask application object"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get local preferences for the user"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """defined the landing with translation"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
