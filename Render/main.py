
from flask import Flask, render_template

# v objektno orientiranem smo naredili Flask
app = Flask(__name__)

# controler = root of the website "/"
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__':
    app.run(port="5001", use_reloader=True)
    
    