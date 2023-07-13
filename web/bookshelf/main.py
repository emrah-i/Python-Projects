from flask import render_template, redirect, request, url_for
from models import app, db, Books, BookForm, Delete
from flask_bootstrap import Bootstrap5
import requests

app.config['SECRET_KEY'] = 'ilovecats'
bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    results = db.session.query(Books.title, Books.author).all()
    books = [f"{row.title} --- {row.author}" for row in results]
    books.insert(0, "")
    add = BookForm()
    delete = Delete()
    delete.book.choices = books
    if request.method == 'POST':
        if add.validate_on_submit() or delete.validate_on_submit():
            type = request.form.get('method')
            if type == 'add':
                    title = add.title.data.strip()
                    author = add.author.data.strip()
                    read = add.read.data
                    response = requests.get(f'https://api.bookcover.longitood.com/bookcover?book_title={title}&author_name={author}')
                    data = response.json()
                    img = data['url']
                    new_book = Books(title=title, author=author, img=img, read=read)
                    db.session.add(new_book)
                    db.session.commit()
                    return redirect('/edit')
            elif type == 'delete':
                    title = delete.book.data.split(' --- ')[0]
                    entry = db.session.query(Books).filter(Books.title == title).first()
                    db.session.delete(entry)
                    db.session.commit()
                    return redirect('/edit')
        else:
            message = "<p style='color:red'>*ERROR*</p>"
            return render_template('edit.html', add=add, delete=delete, message=message)
    else:
        return render_template('edit.html', add=add, delete=delete)

@app.route('/read')
def read():
    results = db.session.query(Books).filter(Books.read == True).all()
    return render_template('books.html', books=results)

@app.route('/unread')
def unread():
    results = db.session.query(Books).filter(Books.read == False).all()
    return render_template('books.html', books=results)

@app.route('/read_list')
def read_list():
    return render_template('books.html')

@app.route('/recommend')
def recommend():
    return render_template('index.html')