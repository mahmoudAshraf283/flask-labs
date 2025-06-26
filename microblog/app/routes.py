from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
def index():
    return '<h1>Hello, Flask!</h1>'

@app.route('/index')
def index_page():
    return render_template('index.html', username='Guest')

@app.route('/user/<string:username>')
def greet_user(username):
    return render_template('index.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}')
        return redirect('/user/' + form.username.data)

    return render_template('login.html', form=form)