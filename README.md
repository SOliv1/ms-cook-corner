# Cook Corner

#### Table Of Contents
* General Information
* Live Demo
* UX Introduction
* User stories
* Wireframe Mockups
* Website & Database
* Accessibility
* Features
* Deployment
* Testing
* Credits
* Conclusion

###  LIVE DEMO CAN BE FOUND AT HEROKU: https://cook-corner-ms.herokuapp.com/

### README  Further information and alternative view via LINK HERE
  README.md https://1drv.ms/w/s!AgMQTPoqZgRAjBzcw6gYVD7gImdt?e=5XbCvm
  
## UX Introduction 
A dynamic website where keen cooks can post recipes and exchange recipe ideas with other cooks.  This website celebrates the tradition of great British craftsmanship and British cooking. 
Mason Cash originated in a pottery operating at Church Gresley in the heart of the English ceramic industry in 1800.
Two hundred years later, 
>mixing practicality with elegance
>is the mantra for this distinctive brand.  
The website is a B2C emotion driven and appeals to the benefits of users by encouraging interaction and engagement through the exchange and addition of favourite recipes on the databse.  This website ideally is a logon and password encrypted one. However, that is left for me to implement later. My focus is on the CRUD functionality.
Bakeware, untensils and beautiful mixing bowls in various colours are available and ready to use by those who appreciate baking and cooking only with the finest!

This website features the iconic mixing bowls which are made from high quality, chip-resistant earthenware making them heavy enough to stand when mixing, yet light enough to hold comfortably in one arm.
The Oven and Bakeware comes in a range of sturdy and durable materials, from cane design bowls, gleaming white linea ovenware, oval and round to rectangular dishes; and finally the warmth of high quality terracotta and porous dishes which absorb moisture from the dough in order to produce a perfect crust every time.  The utensils has been designed for multi-functionality and comfort. Each piece is designed for multi-purpose functionality.  There are two innovative ranges in beechwood and stainless Steel range which ensures that all cooks needs are met.  The recipes are mainly British and in the spirit of well loved recipes old and new, tried and true; this website has been developed.
#### Ideal Customer:
* wants to buy the finest and iconic utensils and cookware. Enjoys cooking, experimenting.
* discover and share new ideas and recipes with keen cooks.
#### Visitors to this website are looking for:
* good quality bowls and utensils to use in recipes in the simple to use database provided and   can be easily be used to **Create, add, edit, update and delete** by the user.
* This website is a design for keen cooks to share recipes with others, by swapping ideas and building up a collection.  
* Visitors have access to all the cook-ware they need via a link on the website to the finest British cookware *Mason Cash*  [Masoncash](https://www.masoncash.co.uk/products/mixing-bowls.html) when only the best will do.
#### This website is best for:
1. A new customer who wants to discover more about the useful implements and products that can be found on the website and buy directly with companies who speicalise in Mason Cash via links. This is in addition to promoting *Mason Cash* the Company, without having to leave the site.
1. As a new visitor to the website I want to be able to navigate quickly and easkily.
1. As an interested visitor / customer I want to follow the activities of this website on social media.
1. As an engaged visitor I want to return to the website and potentially purchase the products and find out what is new.  A contact    	  form and newsletter will be set up for this. 
1. Provide *User-stories adding to the website to encourage new and returning customers.


## User Stories:
* As a customer, I want to be able to quickly look up the best products to use for my recipes, so that I can order via the website from the company. I want to experiement with the recipes: edit / delete / and update with my own versions of a particular recipe. I want to try them out on friends and family. Talk about inspiring recipes with other keen cooks, and add my own recipes  to the mix.  
  *Happy Customer - I. Cook

* I love the look and feel of the website. It is very appealing and harmoniously set up.  I can find everything from the **Mason and Cash Company** here and I adore all things **British**.   The recipes are delicious. I relish trying them out and discussing with other likeminded members here. I love adding recipes to the website as I discover new dishes. A fullfilling hobby!
  *Satisfied Customer - W. E. Bake
  
* I love social media and am looking forward to sharing my recipes with other keen bloggers and social media aficionados! 
 *Love it - S. M. Butterfly
 
* What a pretty website! - so simple to use - I would like to be able to sort recipes and rate them. Looking forward to receiving   newsletters, trying all the mouthwatering dishes and sharing with my friends. 
  *Can't wait  - B. Patience
  
## CookCorner = Wireframes and Mockups:

*Please follow the link below to view wireframes and Mockups*:

[cookCorner](http://github.com/SOliv1/ms-cook-corner/tree/master/wireframes)

			
## Website & Database
I chose Mongo DBAtlas for my project which was recommended by C.I. in the course.
My website Database consists of *Pages (to meet CRUD requirement - Create Read Update Delete) in a database called MONGO DB Atlas* It is a highly scalable server which stores data in a non-relational format.
A *Relational Database(SQL)*  provides commands for creating and modifying databases, as well as querying and modifying data.

#### Add recipe page (‘Create’, 'Read', 'Update', 'Delete')
This is how users add recipes to the database. It contains a simple HTML form to collect the recipe attributes we intend to store. 
The recipe collection in the database should have the same attributes.

## Accessibility 
The pages are asscesible via buttons on the *Home page*. A carousel provides seperate *Create* and *View Recipes buttons. The *Recipes*
menu on the top right corner of the menu(home-page) is where users can view collection of recipes.  This is also accessed via the carousel view recipes button on the *Home page*.  *Add a Recipe* The Edit / Update and delete buttons come into play when user submits (button) Edit / Update pages are brought into view. The delete button removes recipe and returns to home page. The whole process resumes again via pressing *Create* button to add another recipe. The process of populating the database from *fontend* is simple quick and easy to do and fun too.

## Features
The main feature I am showcasing in this website is the CRUD FUNCTIONALITY.  The pages consist of the following:
* A list of ingredients
* A method/list of preparation instructions
* Any other attributes necessary (the number of attributes does not need to be complex, since * * creating a new form element is just about copying and pasting others I create).
* List of recipes page **(‘Read’)*
* This page that displays the recipes in the database. ( this being on home page*).
* The *add_recipe* page which displays the form and the recipe form_request which links to the flask database and then inserts the recipe into the database via the website. 
* The *edit_recipe* page *(‘Update’)*
* A page to edit an existing recipe. This looks exactly the same as the *add recipe* page, except this time, the form is pre-populated with values belonging to the recipe being edited.

Each recipe listed on the `home` page has an *edit button* that links to the `home` page.
Delete link for each recipe *(‘Delete’)*
Each recipe list (on the home page) has a *delete_recipe* button that links to the `delete view`*.

_*Please note :- In the *insert_recipe* function I have copied and modified the *insert_recipe* code in order to insert reicipes and add the ingredients and instructions text line by line to make it easy for the
user to add their own and update recipes in a similar format.  This is so the user finds the format easy to use and not have to think about how it looks on the page.

The *modified code* was copied from student repo "cook_book https://github.com/3PU/cook-book-milestone-project".
        
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

I have attributed this in the credits section below.*_

## Deployment

#### Deployment to Github
* make sure the branch or folder as a publishing source exists in the repository. Example, before  publishing project site from the /docs folder on the master branch of that repository, 
  collaborator must create a /docs folder on the *master* branch of that repository.
* On GitHub, navigate to site's repository.
* Under repository name, click  Settings.
* Under "GitHub Pages", use Source drop-down menu and select a publishing source.
* More information found on Github:
  https://help.github.com/en/github/working-with-github-pages/configuring-a-publishing-    source-for-your-github-pages-site

#### Cloning a repository to GitHub Desktop
I clone one of my Flask mini projects to deploy locally on GitHub desktop. 
On GitHub, I navigate to the main page of the repository.
Under my repository name, I click to clone my repository in Desktop. I follow the prompts in GitHub Desktop to complete the clone.  

###  Basic set up for my CookCorner project
*(see *CRUD functionality notes further down page*)
pip3 install flask
pip3 install flask_pymongo
pip3 install PyMongo
pip3 install dnspython
pip3 freeze > requirement.txt
python3 app.py to run the server and test

#### Deployment to Heroku
Kindly given to me via Anna Greaves(tutor)as I had trouble logging in with previous commands.

#### First we:
 npm install -g heroku

Then, to login, use the command:
heroku login -i * 

#### Clone the repository
Use Git to clone ms-cook-corner's source code to your local machine.
(e.g. GitHub Pages or Heroku).
When trying to deploy my project to Heroku I hit a bug *- AttributeError
AttributeError: 'NoneType' object has no attribute 'categories'*
In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

To resolve this I ...
Different values for environment variables (Heroku Config Vars)?
Different configuration files?

$ heroku git:clone 
Deploy changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

#### Deploy changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

$ git add .
$ git commit -am ""
$ git push heroku master

**Flask** I add all html pages so they can be rendered in *Flask to the Folder Name "templates"*.  Eventually we will be able to deploy this website on Heroku.  More on this later.
I have rendered the home, about and contact pages using flask and basic jinga template language to make it easier to type the paths and render each of the templates.
for example: we add inside the
 *"@href put {{ url_for('index') }}"*. We also do the same for *"about: {{ url_for('about') }}" and "contact: {{ url_for('contact') }} pages*. 
Essentially, Flask looks up our index() and about() views and injects the URL for it into the href.  All works as expected.
Another handy feature of Flask is the ability to detect any errors we might make such as *writing the url for 'home' instead of the url for 'index'*.  Home does not exist but index does and so indicates this error.

**Template Inheritance** Inherits code from other templates, creating a *base template and using {% extends 'base.html' %} in a child template*.

**Passing Data from View to Template**  A very useful feature of using frameworks to actually set data on the server side and get it coming through to the client.
Benefits of using frameworks is the fact that we can actually get server-side code to provide the frontend with data. 
Example:- Go to *app.py*. Then add argument page_title="About"
to return serverside code to the frontend.
@app.route('/about')
def about():
    return render_template("about.html", page_title="About")

**Reducing repetition**  using the *{% %} notation* template tags for statements (not for expressions).
allowing us to use a *for loop* inside our HTML.  Standard Python *for loop* for number in list_of_numbers.
and then need to supply an {%end for%} so that the templating language knows where the *for loop* stops.
Example:- 
{% for number in list_of_numbers %}
    <p>{{ number }}</p> 
{% endfor %}

**The if template tag**
I use `if` statements inside my template. By using the example here:
 {% if some_condition %} tag and the closing {% endif %} tag. 
See this in action by going to *About* section of website.

**Getting Themes**  I have chosen the **Start bootstrap theme *Clean Blog* as featured in *CI lessons on Flask Framework*, for a multi-page website. 
I download the theme by copying the link then go to terminal and mkdir, then cd into it and wget the https://startbootstrap.com/themes/clean-blog/
I then style accordingly.   Unzip package with the *unzip gh-pages.zip* command.

## Existing Features - C.R.U.D. - allows users to add a recipe to store in database, by having them fill out the form.
*CREATE - Add the recipe by following the instructions.  Whole sections can be inserted by following the recipe page setup.
	  add recipe category, description, ingredinents, instructions.  MDB Atlas cleverly preserves the layout of the recipes     	    that are being populated on the database.

READ -    Read through and view all the recipes as a collection or view each recipe individually by clicking buttons. 

EDIT &
UPDATE -  Click the button to edit the page and follow the instructions there.  Then click the UPDATE button 															to save changes.  Then return to 	   Home page to add another recipe by clicking the CREATE BUTTON again.

DELETE	  Press the delete button to undo changes.  


## Existing Features  - An Example
### Feature 1 - allows users X to achieve Y, by having them fill out Z
Below is an example of a user friendly feature for user(X) to achieve(Y)a recipe collection by filling out their favourite recipe/s and sharing on a user friendly website(Z). 
*Please see modified code example below under the heading:-*
at **Further Inspiration and insert recipe idea from following CI Student website**
_Further Inspiration from following CI Student website:_
https://github.com/3PU/cook-book-milestone-project
*code snippets - *modified code in my project app.py - copied from **cook book** (app.py).*  
_*Please note this is also attributed in the credits section.*_

I want to achieve a seemless userfriendly experience whereby a user can easily copy and paste recipes with a minimum of fuss 
and without having to style the recipes in order to save time.  *Editing and updating*  can be done if and when needed in the users own time.
I tried using semi colons and commas to achieve the seemless new line effects in my insert_recipe function, but these did not work well for me so I copied the idea of newline "(/n)" which suits my purposes to easily *insert recipes* and I think to the satisfaction of the end-user.    
					
### Features Left to Implement:
			* Search box to search recipes.
			* Sort code to sort through recipes and categories
			* Login form with password so users sign in securely using the password to access the database.	
			* More links to other companies specialising in Mason Cash and other British products. 						* Links to other specialised recipe sites appropriate to this website.
			* Contact Form to sign up for newsletters.
			* Another possible  feature to be incorporated is to be able to *vote* for favourite recipes and rate			          a specific recipe.
			* Social media and blogs
			* Chat page / Forum

#### Technologies - a possible sample code to use in future:
>  *login snippet* - copied from https://github.com/joanms/recipe->database/blob/master/app.py:
>	if login_user:
            ### If the username is in the database, hash the password entered in the form and 								compare it with the hashed password in the database for that user
            		if bcrypt.hashpw(request.form['password'].encode('utf-8'), 			 			>login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        		### The user sees this message if the username and/or password are invalid
        				flash('Invalid username/password combination.')
    							return render_template('login.html')
#### Libraries / requirements:

		*dnspython==1.16.0
		*Flask==1.1.1
		*itsdangerous==1.1.0
		*pymongo==3.10.1
		*Werkzeug==1.0.0
		*bison==0.1.2
		*click==7.1.1
		*Flask==1.1.1
		*Flask-PyMongo==2.3.0


#### Links to libraries
	
*	https://pypi.org/project/Flask-Bootstrap4/

*	https://www.fullstackpython.com/flask.html

*	https://flask.palletsprojects.com/en/1.1.x/

*	https://www.mongodb.com/cloud/atlas

*	https://www.python.org/


### For CRUD FUNCTIONALITY 
Install flask: pip3 install flask
Create a python file: app.py
Install pynthon: pip3 dnspython

create instance of flask:   import os

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

### JQuery
The project uses JQuery to simplify DOM manipulation.

##Testing
* https://validator.w3.org/nu/#l118c6 - There is further testing wihich needs addressing. 
127.0.0.1 - - [20/Mar/2020 12:05:52] "GET /get_categories HTTP/1.1" 500 -
Encountered:
* 505 error indicates a temporary problem, and sometimes that problem is very temporary. A site might be getting overwhelmed with traffic, for example. So, refreshing the page is always worth a shot. Most browsers use the F5 key to refresh, and also provide a Refresh button somewhere on the address bar. It doesn’t fix the problem very often, but it takes just a second to try.
* Firefox / Chrome / Edge / - All appear to be working as so are the links.

#### Cloning a repository to GitHub Desktop
I clone one of my Flask mini projects to deploy locally on GitHub desktop. 
On GitHub, I navigate to the main page of the repository.
Under my repository name, I click to clone my repository in Desktop. I follow the prompts in GitHub Desktop to complete the clone.  

(e.g. GitHub Pages or Heroku).
When trying to deploy my project to Heroku I hit a bug *- AttributeError
AttributeError: 'NoneType' object has no attribute 'categories'*
In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

To resolve this I ...
Different values for environment variables (Heroku Config Vars)?
Different configuration files?

#### Bugs
While I was trying to connect sensitive info from my flask app into a env.py file, I got the following error:

Traceback (most recent call last):
  File "/workspace/qc-metrics-analyser-4/app.py", line 7, in <module>
    import env
  File "/workspace/qc-metrics-analyser-4/env.py", line 6, in <module>
    os.environ.get["MONGO_URI"] = "mongodb+srv://seqMetRoot:dbconnection"
TypeError: 'method' object does not support item assignment

I managed to fix my problem with my env.py file. I was incorrectly using the get method. os.environ.get["MONGO_URI"] should have been os.environ["MONGO_URI"] .

Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

Slack community - *various borrowed code snippets* See below credits. I often change them
                     when some of the code did not work for me.  However it did
                     lead me on to thinking again about seeing a line of code highlighted in an error I had been seeing, and checking at the bottom of my jinga codes for these errors.
                     This experience gives me more confidence to debug code.

 #### Dashboard - based on:- 
 https://github.com/PrettyPrinted/building_user_login_system/blob/master/start/templates/dashboard.html

#### Recipes Manager - is based on the basic CRUD functionaity putting it altogether mini project featured in Code Institute DataCentric Module
with recipes made up by me as an example. T This feature is a basic functioning recipe website.  New features can easily be added to improve the user experience and functionality.

#### Technologies use and Atlas MongoDB on recommendation by Code Institute for educational purposes.  A good grounding to build upon.
Create recipes by 
Adding categories 
Adding recipes
Editing recipes
Updating recipes
Deleting recipes
Adding category
Editing category
Updating category
Deleting category


#### Excellent project guide by Code Institute Mentor Brian Machira - thank you for his guidance and support.
https://docs.google.com/document/u/0/?authuser=0&usp=docs_web

#### Further Inspiration and ideas from following CI Student website:
insert_recipe code copied and modified from this code below:-

'''
    @app.route("/insert_recipe", methods=["POST"])
    def insert_recipe():
    recipes = mongo.db.recipes

    form_data = request.form.to_dict()

    ingredients_list = form_data["ingredients"].split("\n")
    instructions_list = form_data["instructions"].split("\n")

    the_recipe = recipes.insert_one(
        {
         "category_name": form_data["category_name"],
         "recipe_name": form_data["recipe_name"],
         "image_link": form_data["image_link"],
         "description": form_data["description"],
         "ingredients": ingredients_list,
         "instructions": instructions_list
        }
    )

    return redirect(url_for("view_recipe",
                            recipe_id=the_recipe.inserted_id))
'''                            
`https://github.com/3PU/cook-book-milestone-project`




#### The text for section "About" *history* was copied from the Wikipedia article https://en.wikipedia.org/wiki/Mason_Cash

#### Media
The photos and credits obtained and used in this site were obtained from *Mason Cash ...*
e.g. media - https://www.masoncash.co.uk/media/bannerslider/a/m/amazon-2.jpg

#### Acknowledgements
I received inspiration for this project from:- 

- "*Mason Cash - Buy British*
-   Brian Machira - *CI Mentor*
-   Anthony Herbet-*Pretty Printed, Flask Extensions videos'

- Slack community - *various borrowed code snippets* which I then modify to suit my purposes, although
                     some of the code did not work for me I had to rethink how to improve this.  However it did
                     lead me on to thinking again about seeing a line of code highlighted in an error that i had been    			     		      seeing, and checking at the bottom of my jinja codes for the errors.
                     It also gives me extra confidence to debug code.  


#### Family Hub - more ideas from this website created by Anna Greaves
https://github.com/AJGreaves/familyhub/blob/master/config.py    
Layout ideas / organisation for my website e.g. config.py, pages for my templates.
####README.md inspiration Anna Greaves - Family Portrait.
```

		     
## Conclusion	     
Overall I feel satisfied with my project and enjoyed creating it despite some issues along the way.  It was certainly challenging but I think the effort was worth it.
