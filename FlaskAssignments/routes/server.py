from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', name="Bro")


@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/success/redirect")
def redirecting():
    return redirect('/')

app.run(debug=True)
