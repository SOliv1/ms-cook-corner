import os
import json
from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path

if path.exists("env.py"):
    import env as config

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

MONGO_URI = os.environ.get("MONGO_URI")
SECRET_KEY = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template("/index.html", page_title="Home")


@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("/about.html", page_title="About", company=data)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form["name"]
        ))
    return render_template("/contact.html", page_title="Contact")
 

@app.route('/recipes')
def recipes():
    return render_template("recipes.html", page_title="Recipes")


    """
    recipes adding the CRUD functionality to my recipe to create a database for users, share recipes and 
    find exchange ideas

    """


@app.route('/')
@app.route('/home')
def get_tasks():
    return render_template("recipes.html", 
                           tasks=mongo.db.tasks.find())    


@app.route('/view_recipe_category')
def view_recipe_category(selected_category):
    all_recipes = mongo.db.recipes.find()
    return render_template("view_recipe_category.html",
                           recipes=all_recipes,
                           selected_category=selected_category,
                           page_title=selected_category + "Recipes")                          


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    tasks = mongo.db.recipes
    tasks.insert_one(request_form.to_dict())
    return redirect(url_for('view_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_task = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes

    form_data = request.form.to_dict()

    ingredients_list = request.form_data["ingredients"].split("\n")
    instructions_list = request.form_data["instructions"].split("\n")

    recipe.update({'_id': ObjectId(recipe_id)},
    {
        'category_name': request.form_data('category_name'),
        'recipe_name': request.form_data('recipe_name'),
        'description': request.form_data('description'),
        'ingredients': reques.form_data('ingredients'),
        'method': request.form_data('method')
    })
    return redirect(url_for("recipes",
                            recipe_id=the_recipe.inserted_id)


@app.route("/delete_recipe_name/<recipe_id>")
def delete_recipe_name(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("home"))



@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())



@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories')) 



@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.categories.find_one(
                            {'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))

    

@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))



if __name__ == '__main__':
    app.secret_key = 'some_secret'
    app.run(host=os.environ.get('IP', "0.0.0.0"),
            port=int(os.environ.get('PORT', "8080")),
            debug=True)          