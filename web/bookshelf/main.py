from flask import render_template, redirect, request
from models import app, Book
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')