#!/usr/bin/env python3
"""0x02. i18n"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """render a page using flask"""
    return render_template('0-index.html')


class Config:
    """class defined to configure the flask app"""
    LANGUAGES = ["en", "fr"]
    ['BABEL_DEFAULT_LOCALE'] = 'en'
    ['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


if __name__ == "__main__":
    app.run(debug=True)
