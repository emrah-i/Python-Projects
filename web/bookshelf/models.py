from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, BooleanField, PasswordField, SelectField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db.init_app(app)

def must_equal_validator(form, field):
    if field.data != "ilovecats":
        raise ValidationError("Key is wrong. You cannot edit the database.")

class Books(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(150), unique=True, nullable=False)
    author = Column(String(100))
    img = Column(String(250))
    read = Column(Boolean, default=False)

class BookForm(FlaskForm):
    key = PasswordField('Key:', validators=[DataRequired(), must_equal_validator], render_kw={'placeholder': 'Keyword'})
    title = StringField('Title:', validators=[DataRequired(), Length(min=2, max=150)], render_kw={'placeholder': 'Title'})
    author = StringField('Author:', validators=[DataRequired(), Length(min=2, max=150)], render_kw={'placeholder': 'Author'})
    read = BooleanField('Read')
    submit = SubmitField()

class Delete(FlaskForm):
    key = PasswordField('Key:', validators=[DataRequired(), must_equal_validator], render_kw={'placeholder': 'Keyword'})
    book = SelectField('Book:', validators=[DataRequired()])
    delete = SubmitField(render_kw={'value': 'Delete', 'style': 'background-color: #E74C3C;border-color: #E74C3C'})

class RecommendBook(FlaskForm):
    title = StringField('Title:', validators=[DataRequired(), Length(min=2, max=150)], render_kw={'placeholder': 'Title'})
    author = StringField('Author:', validators=[DataRequired(), Length(min=2, max=150)], render_kw={'placeholder': 'Author'})
    details = TextAreaField('Details:', validators=[DataRequired(), Length(min=2, max=500)], render_kw={'placeholder': 'Enter your reason for recommending'})
    email = EmailField('Your Email:', validators=[DataRequired()], render_kw={'placeholder': 'Your email'})
    send = SubmitField()
