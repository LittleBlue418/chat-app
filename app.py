import os
from datetime import datetime

from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_message(username, message):
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}

    messages.append(messages_dict)


@app.route('/', methods = ["GET", "POST"])
def index():

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")

@app.route('/<username>')
def user(username):
    return render_template("chat.html", username = username, chat_messages = messages)

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