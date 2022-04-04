from flask import Blueprint, render_template,request,flash

auth= Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html",boolean=True)

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        Fname=request.form.get('Fname')
        phone=request.form.get('phone')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        if len(email)<4:
            flash('Email must be greater than 3 characters!',category='error')
        elif len(Fname)<2:
            flash('Name must be greater than 1 character!',category='error')
        elif password1!=password2:
            flash('No match in password',category='error')
        elif len(password1)<7:
            flash('Password should be greater than 6 characters!',category='error')
        else:
           flash('Account created successfully!',category='success')

    return render_template("signup.html")