from flask import redirect, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
from models import app, db, login_manager, Posts, Users
from flask_migrate import Migrate
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app.config['SECRET_KEY'] = 'ilovecats'
csrf = CSRFProtect(app)
migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):
    return Users.get(user_id)

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
    for post in posts:
        post.date = post.date.strftime("%B %d, %Y %I:%M %p")
    
    button = '''
    <div class="d-flex justify-content-center mt-3">
        <button class="btn btn-primary btn-lg" id="all-posts-load-button">Load More</button>
    </div>'''
    return render_template('all.html', posts=posts, heading='All', button=button)

@app.route('/load')
def load():
    start = int(request.args.get('start')) or 0
    end = start + 5

    all_posts = db.session.query(Posts).all()
    posts = []

    for i in range(start, end + 1):
        if len(all_posts) > i:
            all_posts[i] = all_posts[i].__dict__
            print(all_posts[i])
            del all_posts[i]['_sa_instance_state']
            all_posts[i]['date'] = all_posts[i]['date'].strftime("%B %d, %Y %I:%M %p")
            posts.append(all_posts[i])
        else:
            break

    return jsonify(posts)

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

@app.route('/category/<category>')
def category(category):
    posts = db.session.query(Posts).filter(Posts.category == category).limit(6).all()
    for post in posts:
        post.date = post.date.strftime("%B %d, %Y %I:%M %p")

    button = f'''
    <div class="d-flex justify-content-center mt-3">
        <button class="btn btn-primary btn-lg" id="category-load-button" data-category="{category}">Load More</button>
    </div>'''
    return render_template('all.html', posts=posts, heading=category, button=button)

@app.route('/category_load/<category>')
def category_load(category):
    start = int(request.args.get('start')) or 0
    end = start + 5

    all_posts = db.session.query(Posts).filter(Posts.category == category).all()
    posts = []

    for i in range(start, end + 1):
        if len(all_posts) > i:
            all_posts[i] = all_posts[i].__dict__
            print(all_posts[i])
            del all_posts[i]['_sa_instance_state']
            all_posts[i]['date'] = all_posts[i]['date'].strftime("%B %d, %Y %I:%M %p")
            posts.append(all_posts[i])
        else:
            break

    return jsonify(posts)

@app.route('/update/<int:id>', methods=['PATCH', 'GET'])
def update(id):
    return render_template('index.html')

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    return render_template('index.html')
