import flask
import time

app = flask.Flask(__name__)

@app.route("/")
def index():
    return f"<h1 style='color:red'>Welcome to First Flask Powered Web Page {time.ctime()}</h1>"
@app.route("/hello/<string:name>")
def hello(name):
    return f"<h1>Welcome user <b>{name.upper()}</b><h1>"

app.run('localhost', 5000)

