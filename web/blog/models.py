from sqlalchemy import Column, Integer, String
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from flask import Flask
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
db = SQLAlchemy()
login_manager = LoginManager(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blogs.db"
db.init_app(app)

login_manager.login_view = "login"
login_manager.login_message = "You must login to view that content."

categories = ["Personal", "Travel", "Health", "Food", "Lifestyle", "Fitness", "Technology", "Business", "Book Review"]

class Posts(db.Model):
    id = db.Column(Integer(), primary_key=True)
    title = db.Column(String(80), unique=True, nullable=False)
    subtitle = db.Column(String(80), unique=True, nullable=False)
    author = db.Column(String(100), nullable=False)
    body = db.Column(String(1600), unique=True, nullable=False)
    img_src = db.Column(String(), nullable=False)
    date = db.Column(String(), nullable=False)
    category = db.Column(String(), nullable=False)
    __table_args__ = (
        CheckConstraint(
            category.in_(categories),
            name='category_check'
        ),
    )
    comments = db.relationship('Comments', backref='post_comments', lazy=True)

class Comments(db.Model):
    id = db.Column(Integer(), primary_key=True)
    comment = db.Column(String(250), nullable=False)
    author = db.Column(String(), ForeignKey('users.username'), nullable=False)
    post = db.Column(Integer(), ForeignKey('posts.id'), nullable=False)
    date = db.Column(String(), nullable=False)

class Users(db.Model, UserMixin):
    id = db.Column(Integer(), primary_key=True)
    f_name = db.Column(String(), nullable=False)
    l_name = db.Column(String(), nullable=False)
    email = db.Column(String(), unique=True, nullable=False)
    username = db.Column(String(), unique=True, nullable=False)
    password = db.Column(String(80), nullable=False)
    author = db.relationship('Comments', backref='user_comments', lazy=True)
