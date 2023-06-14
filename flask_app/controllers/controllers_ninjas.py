from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import models_dojo, models_ninja


# Ninja Home Page
@app.route('/ninjas')
def ninjas():
    return render_template("new_ninja.html", dojos = models_dojo.Dojo.get_all())

# Route for creating a new ninja
@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    models_ninja.Ninja.save(request.form)
    return redirect('/')

# Route for editing an existing ninja
# @app.route('/ninjas/edit/<ninja_id>')
# def edit_ninja(ninja_id):
#     return render_template("edit_ninjas.html", )

# Route for deleting a ninja
@app.route('/ninja/destroy/<int:id>')
def destroy(id):
    data = {
        "id": id
    }
    models_ninja.Ninja.destroy(data)
    return redirect('/dojos')