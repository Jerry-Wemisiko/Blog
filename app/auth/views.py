from app.email import mail_message
from flask.globals import request
from app.auth.forms import LoginForm, RegistrationForm
from flask import render_template,redirect,url_for,flash
from . import auth
from ..models import User


@auth.route('/login',methods = ['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('blog.index'))

        flash('Invalid username or password')

    title = "Blog login"
    return render_template('auth/login.html',login_form =  login_form,title = title)

@auth.route('/register',methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
           user = User(email = form.email.data, username = form.username.data,password = form.password.data,profile_pic_path= 'photos/unknown.png')
           db.session.add(user)
           db.session.commit()

           mail_message("Welcome to Blog","email/welcome_user")
           return redirect(url_for('auth.login'))
    return render_template('auth/register.html', registration_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
