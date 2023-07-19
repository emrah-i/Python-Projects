from flask import redirect, render_template, request, jsonify, flash
from flask_wtf.csrf import CSRFProtect
from models import app, db, login_manager, Posts, Users, Comments
from flask_migrate import Migrate
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

app.config['SECRET_KEY'] = 'ilovecats'
csrf = CSRFProtect(app)
migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(id):
    user  = db.session.query(Users).filter(Users.id == id).first()
    return user

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    categories = ["Personal", "Travel", "Health", "Food", "Lifestyle", "Fitness", "Technology", "Business", "Book Review"]
    posts = db.session.query(Posts).limit(3).all()
    return render_template('index.html', posts=posts, categories=categories)

@app.route('/login', methods=['POST', 'GET'])
def login():
    
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        user = db.session.query(Users).filter(Users.username == username).first()

        if user is None:
            flash('Username and password do not match.')
            return render_template('login.html')

        elif not check_password_hash(user.password, password):
            flash('Your passwords must match')
            return render_template('login.html')
        
        login_user(user)
        return redirect('/')
    else:
        return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':

        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        if confirm != password:
            flash('Your passwords must match')
            return render_template('register.html')

        new_user = Users()
        new_user.f_name = f_name
        new_user.l_name = l_name
        new_user.email = email
        new_user.username = username
        new_user.password = generate_password_hash(password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect('/')
    else:
        return render_template('register.html')
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route('/all')
def all():
    posts = db.session.query(Posts).limit(6).all()
    
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
            del all_posts[i]['_sa_instance_state']
            posts.append(all_posts[i])
        else:
            break

    return jsonify(posts)

@app.route('/new', methods=['POST', 'GET'])
@login_required
def new():
    if request.method == 'POST':
        new_post = Posts()
        new_post.title = request.form.get('title')
        new_post.subtitle = request.form.get('subtitle')
        new_post.author = request.form.get('author')
        new_post.body = request.form.get('body')
        new_post.img_src = request.form.get('img')
        new_post.category = request.form.get('category')
        new_post.date = datetime.now().strftime("%B %d, %Y %I:%M %p")
        db.session.add(new_post)
        db.session.commit()
        return redirect('/new')
    else:
        categories = ["Personal", "Travel", "Health", "Food", "Lifestyle", "Fitness", "Technology", "Business", "Book Review"]
        return render_template('new.html', categories=categories)

@app.route('/post/<int:id>')
def post(id):
    post = db.session.query(Posts).filter(Posts.id == id).first()
    comments = []
    for comment in post.comments:
        comments.append(comment)
    return render_template('post.html', post=post, comments=comments)

@app.route('/category/<category>')
def category(category):
    posts = db.session.query(Posts).filter(Posts.category == category).limit(6).all()

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
            del all_posts[i]['_sa_instance_state']
            posts.append(all_posts[i])
        else:
            break

    return jsonify(posts)

@app.route('/comment/<int:id>', methods=['POST'])
def comment(id):

    username = request.form.get('username')
    post_id = request.form.get('post')
    body = request.form.get('body')

    new_comment = Comments()
    new_comment.comment = body
    new_comment.author = username
    new_comment.post = post_id
    new_comment.date = datetime.now().strftime("%B %d, %Y %I:%M %p")
    db.session.add(new_comment)
    db.session.commit()
    return redirect(f'/post/{id}')

@app.route('/update/<int:id>', methods=['PATCH', 'GET'])
@login_required
def update(id):
    return render_template('index.html')

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
@login_required
def delete(id):
    return render_template('index.html')
