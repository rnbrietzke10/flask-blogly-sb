"""Seed file to make sample data for db."""

from models import User, Post, Tag, db, PostTag
from app import app
import datetime

# Create all tables
db.drop_all()
db.create_all()

#Make a bunch of users

river = User(first_name="River", last_name="Bottom", image_url="https://images.unsplash.com/photo-1656873186004-f53c335fa348?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwxMHx8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60")
summer = User(first_name="Summer", last_name="Winter", image_url="https://images.unsplash.com/photo-1599420186946-7b6fb4e297f0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxNnx8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60")
joaquin = User(first_name="Joaquin", last_name="Phoenix", image_url="https://images.unsplash.com/photo-1656794302213-04b7913c2507?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyM3x8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60")
octavia = User(first_name="Octavia", last_name="Spencer")
larry = User(first_name="Larry", last_name="David")
kurt = User(first_name="Kurt", last_name="Cobain", image_url="https://images.unsplash.com/photo-1656856981643-6f72f6a1db75?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyOXx8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60")
rain = User(first_name="Rain", last_name="Phoenix", image_url="https://images.unsplash.com/photo-1656831389296-6487c19d21a7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw0Mnx8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60")

db.session.add_all([river, summer, joaquin, octavia, larry, kurt, rain])

db.session.commit()
post_content= "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
# Add a bunch of tags

awesome = Tag(name='awesome')
css = Tag(name="CSS3")
lol = Tag(name="LOL")
js = Tag(name="JavaScript")
data = Tag(name="Databases")
p = Tag(name="Python")
f = Tag(name="Flask")
psql = Tag(name="PostgreSQL")

db.session.add_all([awesome, lol, js, data, f, p, psql])
db.session.commit()



# Make a bunch of posts
p1 = Post(title="Learn about CSS", content=post_content, user_id=1)
p2 = Post(title="Learn Python", content=post_content, user_id=2)
p3 = Post(title="Learn PostgreSQL", content=post_content, user_id=3)
p4 = Post(title="Learn Flask", content=post_content, user_id=2)
p5 = Post(title="Learn Javascript", content=post_content, user_id=4)

db.session.add_all([p1, p2, p3, p4, p5])

db.session.commit()


p1.tag.append(awesome)
p1.tag.append(css)

p2.tag.append(p)


db.session.add_all([p1, p2])

db.session.commit()

