from flask import render_template, redirect
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    
    return render_template("new_ninja.html", dojos = dojo.Dojo.get_all())