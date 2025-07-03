from app import app, db
from flask import render_template, flash, redirect, request
from app.forms import LoginForm, PostForm
from app.models import Post

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


@app.route('/posts')
def show_posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        flash('Post added!')
        return redirect('/posts')
    return render_template('add_post.html', form=form)

@app.route('/delete_post/<int:post_id>')
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted.')
    return redirect('/posts')