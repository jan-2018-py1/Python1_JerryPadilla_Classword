from flask import Flask, render_template, redirect, session, request, flash
from random import *
app = Flask(__name__)
app.secret_key = "wow"


@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = randint(1,11)

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    number = request.form['guess']
    print number

    if session['number'] == int(number):
        session['result'] = 'correct'
        return redirect('/')

    elif session['number'] < int(number):
        session['result'] = 'Too high'
        return redirect('/')

    else:
        session['result'] = 'Too Low'
        return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)
