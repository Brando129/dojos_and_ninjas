from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.models_dojo import Dojo


# Redirect route to Index Page
@app.route('/')
def index():
    return redirect("/dojos")

# Route for Index Page
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos=dojos)

# Route for creating a new Dojo on the index page
@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

# Route for showing a Dojo
@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo = Dojo.get_one_ninja(data))

