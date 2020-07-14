import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path

if path.exists("env.py"):
    import env as config

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_corner'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
category = "mongo.db.categories.find()"
recipes = "mongo.db.recipes.find()"
recipe = "mongo.db.recipe.find()"
mongo = PyMongo(app)

MONGO_URI = os.environ.get("MONGO_URI")
SECRET_KEY = os.environ.get('SECRET_KEY')


@app.context_processor
def inject_categories():
    all_categories = mongo.db.categories.find()
    return dict(categories=all_categories)


@app.route('/')
def index():
    return render_template("/index.html", page_title="Home")


@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("/about.html", page_title="About", company=data)

    """
    recipes adding the CRUD functionality to my recipe to create a users share
    recipes and find exchange ideas
    """
# view all the recipe collections on this page


@app.route('/view_recipes')
def recipes():
    all_recipes = mongo.db.recipes.find()
    return render_template("recipes.html",
                           recipes=all_recipes,
                           page_title="View Recipes")


#  view_recipe page, provides data for select recipe
@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html",
                           recipe=the_recipe,
                           page_title="View Recipe")


#  add_recipe page, provides the data for populating the category form fields
@app.route("/add_recipe")
def add_recipe():
    all_categories = mongo.db.categories.find()
    return render_template("add_recipe.html",
                           categories=all_categories,
                           page_title="Add a Recipe")


# Inserts a new recipe into database by input from the user

@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    form_request = request.form.to_dict()

    ingredients_list = form_request["ingredients"].split("\n")
    instructions_list = form_request["instructions"].split("\n")

    the_recipe = recipes.insert_one(
        {
         "category_name": form_request["category_name"],
         "recipe_name": form_request["recipe_name"],
         "image_link": form_request["image_link"],
         "description": form_request["description"],
         "recipe_ingredients": ingredients_list,
         "recipe_instructions": instructions_list
        }
    )

    return redirect(url_for("view_recipe",
                            recipe_id=the_recipe.inserted_id))


#  edit_recipe page, provides data for populating the formfields

@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    print(the_recipe)
    return render_template("edit_recipe.html",
                           recipe=the_recipe,
                           categories=all_categories,
                           page_title="Edit Recipe")


# Updates the recipe in the database with changes made by the user

@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):

    form_request = request.form.to_dict()
    ingredients_list = form_request["recipe_ingredients"].split("\n")
    ingredients_list = [x.strip() for x in ingredients_list]
    instructions_list = form_request["recipe_instructions"].split("\n")
    the_recipe = mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
            {"$set": {    
                   "category_name": form_request["category_name"],
                   "recipe_name": form_request["recipe_name"],
                   "image_link": form_request["image_link"],
                   "description": form_request["description"],
                   "recipe_ingredients": ingredients_list,
                   "recipe_instructions": instructions_list
            }})

    return redirect(url_for("view_recipe",
                            recipe_id=recipe_id))


# Deletes the selected recipe from database
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.secret_key = 'some_secret'
    app.run(host=os.environ.get('IP', "86."),
            port=int(os.environ.get('PORT', "8080")),
            debug=False)
