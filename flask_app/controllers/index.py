from flask_app import app
from flask import render_template

@app.route('/')
def r_index():
    return render_template('index.html')