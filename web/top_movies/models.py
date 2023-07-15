from main import db, app
from sqlalchemy import Column, Integer, String, Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, BooleanField, PasswordField, SelectField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length
from bs4 import BeautifulSoup
import requests

