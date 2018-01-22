from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = "RuntimeError"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add():

    if len(request.form['name']) < 1:
        flash("Name not valid")
        return redirect('/')
    elif len(request.form['comment']) < 1:
        flash("Comment cannot be blank")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Comment too long")
        return redirect('/')

    # context = {
    #     'name':request.form['name'],
    #     'location':request.form['location'],
    #     'language':request.form['language'],
    #     'comment':request.form['comment'],
    # }

    return render_template('result.html')
    # return render_template('result.html', context=context)
app.run(debug=True)
