# FLASK TEST FILE
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)

# ROUTES
# home page
@app.route('/')
def home():
    return render_template("home.html", title="Home")

# resume page
@app.route('/resume')
def resume():
    return render_template("resume.html", title="Resume")

# lors page
@app.route('/lors')
def lors():
    return render_template("lors.html", title="LORs")

# projects page
@app.route('/projects')
def projects():
    return render_template("projects.html", title="Projects")
