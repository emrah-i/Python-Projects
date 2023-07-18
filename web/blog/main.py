from flask import redirect, render_template, request
from flask_wtf.csrf import CSRFProtect
from models import app, db, Posts

app.config['SECRET_KEY'] = 'ilovecats'
csrf = CSRFProtect(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    categories = ["Personal", "Travel", "Health", "Food", "Lifestyle", "Fitness", "Technology", "Business", "Book Review"]
    posts = db.session.query(Posts).limit(3).all()
    return render_template('index.html', posts=posts, categories=categories)

@app.route('/all')
def all():
    posts = db.session.query(Posts).limit(6).all()
    return render_template('all.html', posts=posts)

@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        new_post = Posts()
        new_post.title = request.form.get('title')
        new_post.subtitle = request.form.get('subtitle')
        new_post.author = request.form.get('author')
        new_post.body = request.form.get('body')
        new_post.img_src = request.form.get('img')
        new_post.category = request.form.get('category')
        db.session.add(new_post)
        db.session.commit()
        return redirect('/new')
    else:
        categories = ["Personal", "Travel", "Health", "Food", "Lifestyle", "Fitness", "Technology", "Business", "Book Review"]
        return render_template('new.html', categories=categories)

@app.route('/post/<int:id>')
def post(id):
    post = db.session.query(Posts).filter(Posts.id == id).first()
    return render_template('post.html', post=post)

@app.route('/update/<int:id>', methods=['PATCH', 'GET'])
def update(id):
    return render_template('index.html')

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    return render_template('index.html')
