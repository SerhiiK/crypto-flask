from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<p>Hello</p>"

@app.route("/about")
def about_page():
    return "<p> Will be filled soon....</p>"
