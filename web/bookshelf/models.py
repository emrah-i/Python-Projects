from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db.init_app(app)

class Book(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(150), unique=True, nullable=False)
    author = Column(String(100), unique=True)
    img = Column(String(250))
    read = Column(Boolean, default=False)