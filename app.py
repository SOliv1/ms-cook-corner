import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html", page_title="About")


@app.route('/contact')
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route('/recipes')
def recipes():
    return render_template("recipes.html", page_title="Recipes")    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)