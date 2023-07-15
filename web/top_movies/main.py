from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ilovecats'
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        type = request.form.get('type')

        if type == 'search':
            title = request.form.get('title')
            url = f"https://api.themoviedb.org/3/search/movie?query={title}"
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZmY3NWFhZWZjN2JhNTcyOTU1Y2NlNzIyODQ0NThhZiIsInN1YiI6IjY0YjFlY2VhZTBjYTdmMDBhZTc0ZTAxZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6p5_kLqkcX9uYw_-6aNdAOSI9a5vxAEpu0S84JPZU98"
            }
            response = requests.get(url, headers=headers)
            data = response.json()
            movies = data['results']
            header = 'Select a Movie'
            comment = 'Select a movie from the list below by clicking on it.'
            return render_template('search.html', header=header, comment=comment, movies=movies)
        else:
            id = request.form.get('movie')
            return redirect(f'/add/{id}')
    else:
        header = 'Search for a Movie'
        comment = 'Search below the title of the movie and a list of results will show.'
        return render_template('search.html', header=header, comment=comment)

@app.route('/add/<int:id>', methods=['POST', 'GET'])
def add(id):
    start = 'https://image.tmdb.org/t/p/w1280/'
    url = f"https://api.themoviedb.org/3/movie/{id}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZmY3NWFhZWZjN2JhNTcyOTU1Y2NlNzIyODQ0NThhZiIsInN1YiI6IjY0YjFlY2VhZTBjYTdmMDBhZTc0ZTAxZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6p5_kLqkcX9uYw_-6aNdAOSI9a5vxAEpu0S84JPZU98"
    }
    response = requests.get(url, headers=headers)
    movie = response.json()
    movie['img_src'] = start + movie['poster_path']
    return render_template('add.html', movie=movie)

@app.route('/update')
def update():
    return render_template('index.html')

@app.route('/delete')
def delete():
    return render_template('index.html')