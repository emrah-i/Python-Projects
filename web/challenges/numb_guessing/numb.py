from flask import Flask, redirect, render_template
from random import *

app = Flask(__name__)

numb = ''

@app.route("/")
def numb_choice():
    global numb
    numb = randint(1, 10)
    return render_template('hello.html')

@app.route("/choice")
def choice():
    if numb == '':
        return redirect("/")
    else:
        return render_template('choice.html')
    
@app.route("/<int:guess>")
def numb_guess(guess):
    print(numb)
    if numb == '':
        return redirect("/")
    else:
        return render_template('guess.html', numb=numb, guess=guess)

if __name__ == '__main__':
    app.run(debug=True)