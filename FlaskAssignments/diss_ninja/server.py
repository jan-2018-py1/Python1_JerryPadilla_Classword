from flask import Flask, redirect, render_template, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    if 'color' in session:
        session.pop('color')
    return render_template('index.html')

@app.route('/ninja')
def ninja():

    if 'color' not in session:
        session['color'] = 'all'

    return render_template('ninja.html')

@app.route('/ninja/<color>')
def color(color):

    if color == 'blue':
        session['color'] = 'blue'
        return redirect('/ninja')
    elif color == 'orange':
        session['color'] = 'orange'
        return redirect('/ninja')
    elif color == 'red':
        session['color'] = 'red'
        return redirect('/ninja')
    elif color == 'purple':
        session['color'] = 'purple'
        return redirect('/ninja')
    else:
        session['color'] = None
        return redirect('/ninja')

    return redirect('/ninja')

app.run(debug=True)
