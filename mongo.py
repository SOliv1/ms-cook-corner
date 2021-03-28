import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

# if path.exists("env.py"):
#   import env as config


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_corner'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
recipes = "mongo.db.recipes.find()"
recipe = "mongo.db.recipe.find()"
mongo = PyMongo(app)

MONGO_URI = os.environ.get("MONGO_URI")
SECRET_KEY = os.environ.get('SECRET_KEY')

@app.route('/')
@app.route('/get_recipes')
def get_tasks():
    return render_template("recipes.html", tasks=mongo.db.tasks.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)