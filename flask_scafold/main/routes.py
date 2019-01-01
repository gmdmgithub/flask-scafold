from flask import render_template, url_for, flash, redirect, Blueprint

main = Blueprint('main',__name__)

@main.route('/')
def hello_world():
    param = {"title":"Some title"}
    return render_template('home.html', param=param)

@main.route("/about")
def about():
    return render_template('about.html', title='About')