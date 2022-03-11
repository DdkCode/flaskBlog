
from flaskblog import app, db
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

import time
time =  time.asctime()[4:]

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", title='Home', timeString = time)


@app.route("/about")
def about():
	return render_template("about.html", title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():

		newUser = User(username=form.username.data, email=form.email.data, image_file='None', password=form.password.data)
		db.session.add(newUser)
		db.session.commit()
		
		flash(f'Account created for \'{form.username.data}\'!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():


		emailList = User.query.filter_by(email=form.email.data).all()
		print(emailList) 
		if len(emailList) == 1:
			password = emailList[0].password
			if password == form.password.data:
				flash(f'You have logged in!', 'success')
				return redirect(url_for('home'))
			else:
				flash('Login unsucessful, incorrect password.', 'danger')
		else:
			flash('Login unsucessful, this user is not recognised.', 'danger')
	
	return render_template('login.html', title='Login', form=form)


@app.route("/boot")
def boot():
	return render_template("bootstrap.html", title = 'Learning Bootstrap')