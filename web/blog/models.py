from sqlalchemy import Column, Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, CheckConstraint
from datetime import datetime
from flask import Flask
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
db = SQLAlchemy()
login_manager = LoginManager()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blogs.db"
db.init_app(app)
login_manager.init_app(app)

categories = ["Personal", "Travel", "Health", "Food", "Lifestyle", "Fitness", "Technology", "Business", "Book Review"]

class Posts(db.Model):
    id = Column(Integer(), primary_key=True)
    title = Column(String(80), unique=True, nullable=False)
    subtitle = Column(String(80), unique=True, nullable=False)
    author = Column(String(100), unique=False, nullable=False)
    body = Column(String(1600), unique=True, nullable=False)
    img_src = Column(String(), unique=False, nullable=False)
    date = Column(DateTime(), default=datetime.now(), nullable=False)
    category = Column(String(), nullable=False)
    __table_args__ = (
        CheckConstraint(
            category.in_(categories),
            name='category_check'
        ),
    )

class Users(db.Model, UserMixin):
    id = Column(Integer(), primary_key=True)
    f_name = Column(String(), unique=False, nullable=False)
    l_name = Column(String(), unique=False, nullable=False)
    email = Column(String(), unique=True, nullable=False)
    username = Column(String(), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
