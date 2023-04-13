from flask import Flask, render_template, flash, url_for, redirect
from config import Config
from forms import (
    LoginForm,
    RegisterForm,
)

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object(Config)
users = {}


@app.route('/')
def home():
    """
    Renders the home page of the web application, displaying the number of registered users.

    Returns:
        A rendered HTML template (home.html) with the number of registered users displayed.
    """
    return render_template('home.html', users_amount=len(users))



@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Renders the registration page of the web application and handles form submission. If the form is
    valid and the username is not already taken, it adds the user data to the users dictionary and
    redirects the user to the login page. If the form is invalid or the username is already taken, it
    renders the registration page with an error message.

    Returns:
        If the form is valid and the username is not already taken, a redirect to the login page.
        Otherwise, a rendered HTML template (register.html) with the registration form displayed.
    """
    global users
    form = RegisterForm()
    if form.validate_on_submit():
        if users.get(form.username.data):
            flash("Username already exists")
            return render_template('register.html', form=form)
        users[form.username.data] = (dict(**form.data))
        # Die Daten in einer Datenbank speichern

        # Bestätigungsmeldung
        message = f'Vielen Dank für Ihre Registrierung, {form.vorname.data}!'
        flash(message=message)
        return redirect(url_for("login"))
    else:
        return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Renders the login page of the web application and handles form submission. If the username is
    not found or the password is incorrect, it renders the login page with an error message. If the
    login is successful, it redirects the user to the home page.

    Returns:
        If the login is successful, a redirect to the home page. Otherwise, a rendered HTML template
        (login.html) with the login form displayed.
    """
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data not in users:
            flash("Username not found")
            return render_template('login.html', form=form)
        elif users[form.username.data]['password'] != form.password.data:
            flash("Wrong password")
            return render_template('login.html', form=form)
        flash("Success login")
        return redirect(url_for("home"))
    return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
    home()

