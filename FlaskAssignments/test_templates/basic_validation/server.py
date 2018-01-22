from flask import Flask, render_template, redirect, session, request, flash
# from random import *
# from datetime import datetime
app = Flask(__name__)
app.secret_key = "wow"

@app.route('/')
def index():


    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    return redirect('/')


app.run(debug=True)
