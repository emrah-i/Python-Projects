from sqlalchemy import Column, Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blogs.db"
db.init_app(app)

class Posts(db.Model):
    id = Column(Integer(), primary_key=True)
    title = Column(String(80), unique=True, nullable=False)
    subtitle = Column(String(80), unique=True, nullable=False)
    author = Column(String(100), unique=True, nullable=False)
    body = Column(String(1600), unique=True, nullable=False)
    img_src = Column(String(), unique=False, nullable=False)
    date = Column(DateTime(), default=datetime.now(), nullable=False)
