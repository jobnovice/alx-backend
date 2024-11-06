#!/usr/bin/env python3
"""0x02. i18n"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    """render a page using flask"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
