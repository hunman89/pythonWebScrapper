from flask import Flask, render_template

app = Flask("Job Scrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    return render_template("search.html")

app.run("0.0.0.0")