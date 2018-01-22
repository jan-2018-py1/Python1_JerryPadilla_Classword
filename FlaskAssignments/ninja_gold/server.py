from flask import Flask, render_template, redirect, session, request, flash
from random import *
from datetime import datetime
app = Flask(__name__)
app.secret_key = "wow"


@app.route('/')
def index():

    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []

    print session['gold']

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")

    building = request.form['building']
    if building == 'farm':
        number = randint(9,20)
        session['gold'] += number
        session['activities'] += [str('Earned {} gold from the {}! {}').format(number, building, time)]
        return redirect('/')
    elif building == 'cave':
        number = randint(4,10)
        session['gold'] += number
        session['activities'] += [str('Earned {} gold from the {}! {}').format(number, building, time)]
        return redirect('/')
    elif building == 'house':
        number = randint(1,5)
        session['gold'] += number
        session['activities'] += [str('Earned {} gold from the {}! {}').format(number, building, time)]
        return redirect('/')
    elif building == 'casino':
        number = randint(-51,50)
        if number < 0:
            session['gold'] += number
            session['activities'] += [str('Lost {} gold from the {}! Sucks Dude... {}').format(number, building, time)]
        else:
            session['gold'] += number
            session['activities'] += [str('Earned {} gold from the {}! {}').format(number, building, time)]
            return redirect('/')


    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
