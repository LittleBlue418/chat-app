import os
from datetime import datetime

from flask import Flask, redirect, render_template

app = Flask(__name__)
messages = []

def add_message(username, message):
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))

def get_all_messages():
    return "<br>".join(messages)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<username>')
def user(username):
    return "<h1>Welcome, {0}</h1> {1}".format(username, get_all_messages())

@app.route('/<username>/<message>')
def send_message(username, message):
    add_message(username, message)
    return redirect("/" + username)

if __name__=="__main__":
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=True
    )