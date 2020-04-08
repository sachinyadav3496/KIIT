
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello/<string:name>")
def hello(name):
    return f"<h1>Welcome user {name}</h1>"
app.run('localhost', 80)
