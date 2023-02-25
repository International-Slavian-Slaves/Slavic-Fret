from flask import render_template

import app


@app.route("/")
def hello():
    return render_template('index.html')
