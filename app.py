"""Blogly application."""

from flask import Flask, redirect, request, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_users_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# connect app to database
connect_db(app)

@app.route('/users')
def list_users():
    users = User.query.all()
    print(users)
    return render_template("users.html", users=users)

@app.route('/')
def base():
    return redirect('/users')


@app.route('/users/new')
def add_new_user_form():
    return render_template('new_user_form.html')

@app.route('/users/new', methods=["POST"])
def add_user():
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    img_url = request.form['imageUrl']
    new_user = User(first_name=first_name, last_name=last_name, image_url=img_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def user_detail_page(user_id):
    """Get user by id and render template with there information"""

    user = User.query.get_or_404(user_id)
    return render_template('user_detail_page.html', user=user)


@app.route('/users/<int:user_id>/edit')
def edit_user_info_page(user_id):
    user = User.query.get(user_id)
    print(user)

    return render_template('edit_user_page.html', user=user)



@app.route('/users/<int:user_id>/edit', methods=["POST"])
def edit_user_info(user_id):
    user = User.query.get(user_id)
    user.first_name =  request.form['firstName']
    user.last_name =  request.form['lastName']
    user.image_url =  request.form['imageUrl']
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')