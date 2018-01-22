from flask import Flask, render_template, redirect, request, flash, session
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "RuntimeError"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/validate', methods=['POST'])
def validate():

    if len(request.form['email']) < 1:
        flash(u'Must Enter Email','error')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash(u'Not a valid Email','error')
        return redirect('/')
    elif len(request.form['first_name']) < 1:
        flash(u'Must Enter Name','error')
        return redirect('/')
    elif len(request.form['last_name']) < 1:
        flash(u'Must Enter Last Name','error')
        return redirect('/')
    elif len(request.form['password']) < 8:
        flash(u'Password Must be at least 8 Char','error')
        return redirect('/')
    elif request.form['password'] != request.form['confirm_password']:
        flash(u'Password does not match','error')
        return redirect('/')
    else:
        flash("Thank you for submitting your info")
        return redirect('/')

    # context = {
    #     'name':request.form['name'],
    #     'location':request.form['location'],
    #     'language':request.form['language'],
    #     'comment':request.form['comment'],
    # }


    # return render_template('result.html', context=context)
app.run(debug=True)
