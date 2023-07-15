from flask import Flask
from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db.init_app(app)

class Movies(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=False)
    title = Column(String(150), unique=True, nullable=False)
    release = Column(String(12))
    description = Column(String(500))
    img = Column(String(250))
    comment = Column(String(150))
    rating = Column(Float)