from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app.forms.LoginForm import LoginForm
from app.forms.RegistrationForm import RegistrationForm
from app.models.User import User
from app import db


def register():
   if not current_user.is_authenticated:
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
   return redirect(url_for('index_bp.home'))


def login():
   if not current_user.is_authenticated:
      form = LoginForm(request.form)
      if request.method == "POST":
         if form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user.verify_password(form.password.data):
               login_user(user, remember=form.remember_me.data)
               flash(f"Logged in successfully!", "positive")
               return render_template('home.html')
      
      return render_template('login.html', form=form)
   return redirect(url_for('index_bp.home'))

@login_required
def logout():
   logout_user()
   return redirect(url_for('index_bp.home'))