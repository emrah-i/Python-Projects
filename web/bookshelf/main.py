from flask import render_template, redirect, request
from models import app, Book
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    return render_template('index.html')

@app.route('/read')
def read():
    return render_template('index.html')

@app.route('/unread')
def unread():
    return render_template('index.html')

@app.route('/read_list')
def read_list():
    return render_template('index.html')

@app.route('/recommend')
def recommend():
    return render_template('index.html')