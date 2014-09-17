#! /usr/bin/python
from flask import Flask
from flask import render_template

app = Flask(__name__)

data = open("data.txt", 'r').read().split("\n")

import cgi
@app.route("/")
def mainpage():
    return render_template("Pokemon.html")

@app.route("/<int:pokemonid>")
def search(pokemonid):
    source = data[pokemonid].split(",")
    pid = source[0]
    name = source[1]
    return render_template("id.html", pid=pid, name=name)

if __name__ == "__main__":
    app.run(debug=True)
