from flask import redirect, render_template
from models import app, db, Posts

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all')
def all():
    return render_template('all.html')

@app.route('/new', methods=['POST', 'GET'])
def new():
    return render_template('new.html')

@app.route('/post/<int:id>')
def post(id):
    return render_template('post.html')

@app.route('/update/<int:id>', methods=['PATCH', 'GET'])
def update(id):
    return render_template('index.html')

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    return render_template('index.html')
