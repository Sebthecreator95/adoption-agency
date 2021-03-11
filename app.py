from flask import Flask, url_for, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "TopSecret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
connect_db(app)
db.create_all()


@app.route("/")
def pets():
    """List all pets."""
    pets = Pet.query.all()
    return render_template("pets.html", pets=pets)


@app.route("/addpet", methods=["GET", "POST"])
def add_pet_form():
    """Add a pet."""
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(name = form.name.data, species =form.species.data, photo_url=form.photo_url.data, age=form.age.data, notes=form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Your post was succesfuly added")
        return redirect("/")

    else:
        return render_template("addPetForm.html", form=form)


@app.route("/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect("/")

    else:
        return render_template("editPetForm.html", form=form, pet=pet)


@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "species": pet.species, "age": pet.age, "notes": pet.notes, "available": pet.available, "photo_url": pet.photo_url}

    return jsonify(info)