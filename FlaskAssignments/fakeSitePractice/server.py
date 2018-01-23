from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "Secret"


# This fake site uses session to store an email and password. This site does not encrypt passwords. The password will be in plain text. This is just to practice fundamentals.



@app.route('/')
def index():
    if 'login' not in session:
        flash('Need to login or Register')
        return redirect('/login')
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

    # I know I can have both register and login on the same html page.

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/process_register', methods=['POST'])
def process():

    # Validates and creates session data based off form data

    if len(request.form['email']) < 1:
        flash('Email must be valid')
        return redirect('/register')
    elif len(request.form['password']) < 8:
        flash('Password must be at least 8')
        return redirect('/register')
    elif request.form['password'] != request.form['confirm_password']:
        flash('Passwords must match')
        return redirect('/register')
    else:
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        flash('Thanks for registering! Now please login.')
        return redirect('/login')

@app.route('/process_login', methods=['POST'])
def process_login():

    # Gets a bug when processing login info when session['email'], session['password'] don't have anything stored through "process_register". Meaning if you clear the session then try and login, it bugs out because recog session yet. If nothing is in session for the first login attempt then it bugs out on the 'email' validation because there is no session['email'] yet

    if 'email' not in session:
        flash('No account registered with those creds')
        return redirect('/')
    elif 'password' not in session:
        flash('No account registered with those creds')
        return redirect('/')


    # validates form data and determines if it matches the fake session/"database"

    if len(request.form['email']) < 1:
        flash('Email must be valid')
        return redirect('/login')
    elif len(request.form['password']) < 8:
        flash('Password must be at least 8')
        return redirect('/login')

    if request.form['email'] == session['email']:
        if request.form['password'] == session['password']:
            session['login'] = 'login'
            flash('You successfully logged the fuck in')
            return redirect('/')
        else:
            flash('Incorrect Email or Password')
            return redirect('/login')
    else:
        flash('Incorrect Email or Password')
        return redirect('/login')

@app.route('/logout')
def logout():
    # This will clear the login session forcing you back to login screen
    session.pop('login')
    return redirect('/')

@app.route('/clear_all')
def clear_all():
    # This will clear all session
    session.clear()
    return redirect('/')

app.run(debug=True)
