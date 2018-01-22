from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "counter"


@app.route('/')
def index():

    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1

    return render_template('index.html')

@app.route('/add')
def add():
    session['count'] +=1

    return redirect('/')

@app.route('/pop')
def pop():
    for key in session.keys():
        session.pop(key)

    return redirect('/')

app.run(debug=True)
