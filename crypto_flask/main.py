from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('home.html')

@app.route("/about")
def about_page():
    return "<p> Will be filled soon....</p>"
