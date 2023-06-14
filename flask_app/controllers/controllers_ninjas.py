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
@app.route('/ninjas/edit/<int:id>')
def edit_ninja(id):
    data = {
        "id": id
    }
    return render_template("edit_ninjas.html", ninja = models_ninja.Ninja.get_one(data))

# Route for updating the edited ninja
@app.route('/ninja/update', methods=['POST'])
def update():
    models_ninja.Ninja.update(request.form)
    return redirect('/dojos') #this url needs fixed

# Route for deleting a ninja
@app.route('/ninja/destroy/<int:id>')
def destroy(id):
    data = {
        "id": id
    }
    models_ninja.Ninja.destroy(data)
    return redirect('/dojos')