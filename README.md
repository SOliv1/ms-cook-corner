## Cook Corner
A dynamic website where interested cooks can post recipes and exchange recipe ideas with other cooks.  This website celebrates the tradition of great British craftsmanship. 
Mason Cash originated in a pottery operating at Church Gresley in the heart of the English ceramic industry in 1800.
Essentially, this part is your sales pitch. Two hundred years later mixing practicality with elegance is the mantra for this iconic brand.
Bakeware, untensils and beautiful mixing bowls in various colours are available and ready to use by those who appreciate baking and cooking only with the finest!

The famous mixing bowls are made from high quality, chip-resistant earthenware making them heavy enough to stand when mixing, yet light enough to hold comfortably in one arm.
The Oven and Bakeware comes in a range of sturdy and durable materials, from cane design bowls, gleaming white linea ovenware, oval and round to rectangular dishes; and finally the warmth of 
high quality terracotta and porous dishes which absorb moisture from the dough in order to produce a perfect crust every time.

The utensils has been designed for multi-functionality and comfort. Each piece is designed for multi-purpose functionality.  
There are two innovative ranges in beechwood and stainless Steel range which ensures that all cooks needs are met.

## UX
This website is designed for keen cooks to share recipes with others, by swapping ideas and building up a collection.  They have access to all the cook ware they need
via a link on the website to the finest British cookware *Mason Cash* when only the best will do.
I want to find out more about the useful implements and products that can be found on the website and buy directly with companies who speicalize in Mason Cash as well as promoting *Mason Cash* the Company, without having to leave the site.
In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.
static/img/wirefme1.png 
static/img/wirefme2.png

## Features

### Website

### Deployment to Heroku
Kindly given to me via Anna Greaves(tutor)as I had trouble logging in with previous commands.

*Here we go:
 npm install -g heroku

Then, to login, use the command:
heroku login -i * 

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

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

## Existing Features
Feature 1 - allows users X to achieve Y, by having them fill out Z
...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

## Features Left to Implement
# Flask Chat project in my Recipe application
I originally cloned from my previous Flask Chat Project to build and create features in my new
Milestone 3 project. This chat application was written in *Flask*.  The application was downloaded from the libruaries using the pip3 install Flask from flask command.
The purpose of this project is to take data from a URL and store the information in a list, in this case sharing recipe ideas with authorised users who have signed up 
for this service.



Another feature idea
##Technologies Used

###For CRUD FUNCTIONALITY 
Install flask: pip3 install flask
Create a python file: app.py
Install pynthon: pip3 dnspython

create instance of flask:   import os

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

## JQuery
The project uses JQuery to simplify DOM manipulation.
## Testing
127.0.0.1 - - [20/Mar/2020 12:05:52] "GET /get_categories HTTP/1.1" 500 -
Encountered:
505 error indicates a temporary problem, and sometimes that problem is very temporary. A site might be getting overwhelmed with traffic, for example. So, refreshing the page is always worth a shot. Most browsers use the F5 key to refresh, and also provide a Refresh button somewhere on the address bar. It doesn’t fix the problem very often, but it takes just a second to try.


In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

## Contact form:
### Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.
 
## Deployment
### Cloning a repository to GitHub Desktop
I cloned one of my Flask mini projects to deploy locally on GitHub desktop. 
On GitHub, I navigate to the main page of the repository.
Under my repository name, I click to clone my repository in Desktop. I follow the prompts in GitHub Desktop to complete the clone.  




This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?

###bugs
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

## Credits
###Content
### Cook Corner - Home page image - curtesy of Mason Cash:- 
 https://www.masoncash.co.uk/index.php/prodsecucts/mixing-bowls/colour-mix-mixing-bowls.html

#### About Page - all image credits curtesy of *Mason Cash*.  About main section copied from Wikipedia; https://en.wikipedia.org/wiki/Mason_Cash
*Featurette images and accompanying product information on mixing bowls credited to *Mason Cash* - https://www.masoncash.co.uk/products/mixing-bowls.html
Second image curtesy of *Dunelm*:- https://i1.adis.ws/i/dm/30563229.jpg?$standardplayerzoom$&img404=noimagedefault
#### Login - copied code from:
- https://www.youtube.com/watch?v=vVx1737auSE

- and *login snippet* - copied from https://github.com/joanms/recipe-database/blob/master/app.py:
if login_user:
            ### If the username is in the database, hash the password entered in the form and compare it with the hashed password in the database for that user
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        ### The user sees this message if the username and/or password are invalid
        flash('Invalid username/password combination.')
    return render_template('login.html')
    and also 
- *code also taken from* 
 https://github.com/PrettyPrinted/mongodb-user-login/blob/master/login_example.py

 #### Dashboard - based on:- 
 https://github.com/PrettyPrinted/building_user_login_system/blob/master/start/templates/dashboard.html

##### Recipes Manager - is based on the basic CRUD functionaity putting it altogether mini project featured in Code Institute DataCentric Module
with recipes made up by me as an example. T This feature is a basic functioning recipe website.  New features can easily be added to improve the user experience and functionality.
#####Technologies used Atlas MongoDB recommended by Code Institute
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

A nice feature to be incorporated - be able to vote in different recipes and be more specific on recipe ingredients.


###Family Hub created by Anna Greaves
https://github.com/AJGreaves/familyhub/blob/master/config.py    
Layout ideas / organisation for my website e.g. config.py, pages for my templates

''The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from ...
Acknowledgements
I received inspiration for this project from X