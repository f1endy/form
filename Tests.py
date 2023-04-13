# n = int(input())
# l = []
# if n % 2 != 0:
#     print(l)
#
#
# def is_prime(x):
#     if x == 1:
#         return False
#     for i in range(2, n // 2):
#         if x % i == 0:
#             return False
#         else:
#             continue
#     return True
#
#
# for i in range()


# l = [-5, -3, -1, 0, 3, 4, 6 , 7, 10]
# n = 7
#
#
# def binary_search(array, x):
#     check = 0
#     low = 0
#     high = len(array) - 1
#     while True:
#         mid = low + (high - low) // 2
#         if array[mid] + check == x:
#             print(array[check], array[mid])
#             check += 1
#             low = check
#             high = len(array) - 1
#
#         elif array[mid] + check < x:
#             low = mid + 1
#         elif array[mid] + check > x:
#             high = mid - 1
#         if mid + 1 == high and mid - 1 == low:
#             check += 1
#             low = check
#             high = len(array) - 1
#             return
#
#
# binary_search(l, n)
#
# from random import randint
#
# import os
# class My_file:
#
#     def __init__(self, name):
#         self.name = name
#
#     def path(self):
#         print(os.path.abspath(self.name))
#
#     def extension(self, ext):
#         self.name[self.name.find(".")] = "ext"
#
#
# file = My_file("doc.txt")
# file.extension("exe")


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
    return render_template('home.html', users_amount=len(users))


@app.route('/register', methods=['GET', 'POST'])
def register():
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

# <form method="POST" action="/register">
#     <label for="anrede">Anrede:</label>
#     <select name="anrede" id="anrede">
#         <option value="Herr">Herr</option>
#         <option value="Frau">Frau</option>
#     </select>
#     <br>
#     <label for="vorname">Vor
