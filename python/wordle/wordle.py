from flask import request
from flask import Flask
from flask import render_template
import json

app = Flask(__name__)
data=set()
with open('words.txt', 'r') as file:
    data = json.loads(file.read())

@app.route("/")
def load_front():
    return render_template('wordle.html')

@app.route("/exclude", methods=["POST"])
def exclude():
    valid=set(request.form["valid"])
    invalid=set(request.form["invalid"])
    possibilites=[]
    for word in data:
        w=set(word)
        if valid.issubset(w) and invalid.isdisjoint(w):
            possibilites.append(word)
    return json.dumps(possibilites)
