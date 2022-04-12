from flask import Blueprint, render_template

views= Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")


 

@views.route('/jewellery')
def jewellery():
    return render_template("jewellerypage.html")

@views.route('/bag')
def bags():
    return render_template("bag.html")

@views.route('/decoratives')
def decoratives():
    return render_template("decoratives.html")

@views.route('/saree')
def saree():
    return render_template("saree.html")
