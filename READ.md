### HOW TO CREATE AN APP INSIDE A DJANGO PROJECT
python manage.py startapp <nameoftheapp>

### DJANGO APP FILES
1. migrations/: database migration files (empty initially)
2. __init__.py : indicates the app is a python application
3. admin.py : used to register models for the django admin panel
4. apps.py : contains the app configuration
5. models.py : defines the database models (tables)
6. tests.py : contains test cases for the app
7. views.py : handle request-response logic (functional/controller)
8. urls.py (manually created on app level) : define url patterns for the app

### JINJA TEMPLATING
This is a syntax used to create django interfaces
- To create templates
a. Inside the app folder create a templates folder
b. Inside the templates folder you can create .html files, .css, .js
c. to consolidate the templating for our project, modify the following
- set a global templates directory for referencing our templates i.e. move the todolist templates folder 
  to the global perspective i.e root directory level
- register this change in settings.py for the project under the templates directory settings
        'DIRS': [BASE_DIR / 'templates'], #Add this line

##  DATABASES
organized collection of data that allows users to store, retrieve, update and delete information more efficiently.

## TYPES OF DATABASES
1. Relational Databases
store data in tables:rows(records) and columns(fields) tables and columns
tables can be related
2. NoSQL Databases
3. In-Memory Databases
### WHY USE DB's
1. Persistent data storage
2. Efficient data retrieval
3. Data relationship
4. Security and integrity
### USING DB's IN DJANGO
1. Define our Model data
2. use django migration commands to convert our models into actual database tables
3. Object Relational Mappers (ORM'S) to interact with the db using python code instead
of raw SQL statements
### TO CONVERT MODELS TO TABLES
1. python manage.py makemigrations app name
2. python manage.py migrate

### STEPS TO INCLUDE OB PERSISTENCY FOR PROJECTS IN DJANGO
models.py: converted to db tables by django
After defining our models.py
1/python manage.py makemigrations appname
2/python manage.py migrate

### STEPS TO ADD A DATA SOURCE
1. Double click on the db.sqlite3 file
2. Or simply from pycharm select the database icon
3. click the + sign or the prompt to create the data source
   (for development use sqlite3)

### RELATION DATABASES : DATABASE RELATIONSHIPS
1. One to many relationship
 - Taskers table (contain the users who will perform the tasks)
 - Task table (Contain the tasks)
To establish a one to many relationship establish a Foreignly

### HOW TO ADD IMAGES (STATIC)
1. Django uses static directory
project-root directory/ => static => images/=>
2. Add {% load static %} at the top of the html file
3. Add this to the settings.py
    STATIC_URL = 
remember to import os''

### DJANGO ADMIN
Create a super user for content management purposes
1. Register your models in admin.py
2. Creating a super admin user for the project

python manage.py createsuperuser
3. Visit the link appurl/admin - use the superuser credentials to login


### DJANGO APIS
Is a set of rules that allows differet software apps to communicate with each other
### Think of an API as a waiter in a restaurant
1. You(Frontend/client) make an order(request)
2. The waiter(API) takes the request to the kitchen(server/backend)
3. The kitchen(server) prepares the food(process the request)
4. The waiter(API) brings back the meal(response) to you

### TYPES OF APIS
1. REST API => Uses HTTP methods ::
- GET :: use this to request data from servers (default)
- POST :: use this to save or send data to servers
- PUT :: use this to upsate on data on servers
- PATCH :: use this to update only a section of your data
- DELETE :: use this to remove data from your servers
2. GraphQl API => Allows clients/frontend to access data only when needed
3. SOAP API => Uses XML methods / older (secure)
4. WebSocket API => Enable real time data transfer (chat applications)

## STEPS TO CREATE AN API PROJECT IN DJANGO
1. Install djangorestframework :: pip install djangorestframework
2. Add djangorestframework as part of the installed apps
3. Have views return data as .json files 
4. Create serializers (picking the data to showcase from the API)
In tne app project create a serializers.py file
### JSON (JavaScript object notation)
This is an interchangeable data format that can be used across any application

### COMMANDS
1. python manage.py startapp todolistappapi
2. pipinstall djangorestframework
3. pip install djangorestframework or pipx install djangorestframework-include deps python3


FrontEnd(HTML <CSS (web), Android(jetpack compose), React Native, Reactjs) =>
=> middleware => backend (server scripting(python->django), database)

EMOBILIS DATABASE: -student table: name,role,phone,student id
                   -staff table: name,role,phone, staff id
                   -assets: name,price,serial number

### TESTS
1. http://127.8.0.1:8000/ :: web app
2. http://127.8.0.1:8000/api/tasks/ :: API project
3. http://127.8.0.1:8000/admin :: Admin project 


sighn up to postman.com and create an account. Log in to the account

-click on the link for workspace/ if its not there then create a work space. once created select
 a blank workspace ( write the name of the workspace: django API)
select internal then create
make sure you download a postman

1. search for postman desktop agent
-clickpostman agent then download for windows/ set up file
-Do not install anything, don't change anything just select next until it installs
2. download insomnia app/ insomnia.rest
-select hobby
- select to hobby package
-then look for app itself and download it then install it
- do not change anythin when installing it, just click next until it installs

### AUTHENTICATION AND AUTHORIZATION
- Authentication :: IDENTITY MANAGEMENT :: WHO IS USING THE TASK
- Authorization :: USER PRIVILEDGES :: WHAT USER CAN DO ONCE AUTHENTICATED

### STEPS IN CREATING AN AUTHENTICATION MODULE
1. Within settings.py of the project modify the authentication settings
   a. LOGIN_URL :: redirect unauthenticated users back to the log in screen
   b. LOGIN_REDIRECT_URL :: ## After log in what page will the user see
   c. LOGOUT_REDIRECT_URL :: ## After logout, redirect user to log in screen
2. Create views function for the register, login and logout processes
3. create the rendered/ redirected templates
4. Register the urls to map to the authentication functions in views
5. Do migrations :: python manage.py migrate

### EXTENDING THE DJANGO AUTH MODEL
1. Import the class AbstractUser in our models.py
2. Create the custom user class, name should be CustomUser
3. Tell django to use the custom model for the user :: settings.py
4. Update our forms to also use the custom model
   a. create a forms.py in the app folder, write out our custom user form
5. Update the views function to use the custom model / form
6. Updating the templates to reflect the new inputs :: register.html
7. Ensure that our django can handle media
   a. inside settings.py media_url, media_root
   b. urls.py include the media reference as part of the urlpatterns
8. Reset the database and make new migrations
    - delete the migrations folder
    - python manage.py migrate todolistapp zero
    - python manage.py makemigrations appname
    - python manage.py migrate




