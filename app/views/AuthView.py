from flask import flash, render_template, request
from app.forms.RegistrationForm import RegistrationForm
from app.models.User import User
from app import db


def register():
   form = RegistrationForm(request.form)
   if request.method == "POST":
      if form.validate():
         user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
         )
         db.session.add(user)
         db.session.commit()
         # flash('Account successfully created!', category='success')
         return render_template('home.html')

   return render_template('register.html', form=form)