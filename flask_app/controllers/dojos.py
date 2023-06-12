from flask import Flask,render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Dojo


from flask_app.models.dojo import Dojo

# Home Page
@app.route('/')
def index():
    return redirect("/dojos")

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)