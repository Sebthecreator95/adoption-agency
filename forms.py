from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired(message="Please Enter A Name")])

    species = StringField("Species", validators=[InputRequired(message="A species is required")])

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    age = SelectField("Age", choices=[("Newborn","Newborn"), ("Young","Young"), ("Teen","Teen"), ("Adult","Adult")])

    notes = TextAreaField("notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired(message="Please Enter A Name")])

    species = StringField("Species", validators=[InputRequired(message="A species is required")])

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    age = SelectField("Age", choices=[("Newborn","Newborn"), ("Young", "Young"), ("Teen","Teen"), ("Adult", "Adult")])

    notes = TextAreaField("notes", validators=[Optional()])
    
    available = BooleanField("Available?")
