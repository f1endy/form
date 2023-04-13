from wtforms import fields, validators
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = fields.StringField(validators=[DataRequired()])
    password = fields.PasswordField(validators=[DataRequired()])
    submit = fields.SubmitField()


class RegisterForm(FlaskForm):
    username = fields.StringField(validators=[DataRequired()])
    anrede = fields.RadioField(validators=[DataRequired()], label="Anrede", choices=["Herr", "Frau", "Divers"])
    vorname = fields.StringField(validators=[DataRequired()])
    nachname = fields.StringField(validators=[DataRequired()])
    geburtsdatum = fields.DateField(validators=[DataRequired()])
    strasse_hausnummer = fields.StringField(validators=[DataRequired()], label="Straße, Hausnummer")
    plz = fields.StringField(validators=[DataRequired()], label="PLZ")
    ort = fields.StringField(validators=[DataRequired()])
    staatsbuergerschaft = fields.StringField(validators=[DataRequired()])
    password = fields.PasswordField(validators=[DataRequired()])
    confirm = fields.PasswordField(validators=[DataRequired(), validators.EqualTo('password', message='Passwörter stimmen nicht überein!')])
    email = fields.StringField(validators=[DataRequired(), validators.Email(message='Ungültige E-Mail Adresse!')])
    submit = fields.SubmitField()
