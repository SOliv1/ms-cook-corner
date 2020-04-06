import os
import json
from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from os import path

if path.exists("env.py"):
    import env as config


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_corner'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
mongo = PyMongo(app)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return render_template("/index.html")


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

    """
    recipes adding a login and registration to my recipe-pge to create a database for users, share recipes and 
    find exchange ideas
    code based on https://github.com/PrettyPrinted/mongodb-user-login/blob/master/login_example.py
 
   """


@app.route('/')
def login():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')


@app.route('/login', methods=['POST'])
def signin():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('login.html'))

    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('register.html'))
        
        return 'That username already exists!'

    return render_template('register.html')

 

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



@app.route('/recipes')
def recipes():
    return render_template("recipes.html", page_title="Recipes")


    """
    recipes adding the CRUD functionality to my recipe to create a database for users, share recipes and 
    find exchange ideas

    """


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", 
                           tasks=mongo.db.tasks.find())


@app.route('/add_task')
def add_task():
    return render_template('addtask.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edittask.html', task=the_task,
                           categories=all_categories)


@app.route('/update_task/<task_id>', methods=["POST"])
def update_task(task_id):
    tasks = mongo.db.tasks
    tasks.update({'_id': ObjectId(task_id)},
    {
        'task_name': request.form.get('task_name'),
        'category_name': request.form.get('category_name'),
        'task_description': request.form.get('task_description'),
        'due_date': request.form.get('due_date'),
        'is_urgent': request.form.get('is_urgent') 
    })
    return redirect(url_for('get_tasks'))


@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.delete_task({'_id': ObjectId(task_id)})
    return redirect(url_for('get_tasks'))


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


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')    


if __name__ == '__main__':
    app.secret_key = 'some_secret'
    app.run(host=os.environ.get('IP', "0.0.0.0"),
            port=int(os.environ.get('PORT', "8080")),
            debug=True)          