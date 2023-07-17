from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quotes.db"
db.init_app(app)

class Quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(), unique=True, nullable=False)
    author = db.Column(db.String(), unique=True, nullable=False)

with app.app_context():
    db.create_all()
    all = db.session.query(Quotes).all()
    all_quotes = []
    for row in all:
        id = row.id
        quote = row.quote
        author = row.author
        all_quotes.append({
            'id': id,
            'quote': quote,
            'author': author
        })

@app.route('/quotes')
def quotes():
    return jsonify(all_quotes)

@app.route('/random')
def random():
    rand_q = choice(all_quotes)
    return jsonify(rand_q)

@app.route('/search')
def search():
    query = request.args.get("q")
    query_all = []
    for entry in all_quotes:
        ans = entry['author'].lower().find(query.lower())
        ans2 = entry['quote'].lower().find(query.lower())
        if ans != -1:
            query_all.append(entry)
        elif ans2 != -1:
            query_all.append(entry)
    return jsonify(query_all)

@app.route('/new', methods=['POST'])
def new():
    s_quote = request.args.get("quote")
    s_author = request.args.get("author")
    new_q = Quotes()
    new_q.quote = s_quote
    new_q.author = s_author
    db.session.add(new_q)
    db.session.commit()

    return jsonify({'response': {
        'success': 'Quote successfully added.'
    }})

@app.route('/change/<int:id>', methods=['PATCH'])
def change(id):
    c_quote = request.args.get("quote")
    c_author = request.args.get("author")
    item = db.session.query(Quotes).filter(Quotes.id == id).first()
    
    if c_author != None:
        item.author = c_author
    if c_quote != None:
        item.quote = c_quote
    
    db.session.commit()

    return jsonify({'response': {
        'success': 'Item successfully updated.'
    }})

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    item = db.session.query(Quotes).filter(Quotes.id == id).first()
    db.session.delete(item)
    db.session.commit()

    return jsonify({'response': {
        'success': 'Item successfully deleted.'
    }})

