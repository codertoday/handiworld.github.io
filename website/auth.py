from flask import Blueprint, render_template,request,flash,url_for,redirect
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db

auth= Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html",boolean=True)

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName=request.form.get('firstName')
        phoneno=request.form.get('phoneno')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        if len(email)< 4:
            flash("Email must be greater than 3 characters!",category='error')
        elif len(firstName)<2:
            flash("First Name must be greater than 1 characters!",category='error')
        elif len(phoneno)!=10:
            flash("Phone number must be equal to 10 characters!",category='error')
        elif password1!=password2:
            flash("Passwords Don't match!",category='error')
        elif len(password1)<8:
            flash("Password must be atleast of 8 characters!",category='error')
        else:
            new_user= User(email=email,firstName=firstName,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!',category='success')
            return redirect(url_for('views.home'))
            
    return render_template ("signup.html")