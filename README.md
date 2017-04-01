############
Introduction
############
This simulation platform is a technical test for Simudyne company based in London. 
I want to thank Jonathan BAKER & John ANDREWS for this oppotunity. 
I also want to thank Anton IPPOLITOV for the introduction he gave me to them.
The platform works fine on Chrome/Firefox/Safari but not on Opera


############
Technologies
############
As Anton told me not to use PHP, I decided to use a Python framework as python is the language I'm the most using for the last three months. So I used:
	-Python
	-Django framework
	-SQLite
	-HTML
	-CSS
	-JS,
	-Bootstrap



#########
Structure
#########
I used tree command inside the root folder to get it.
If you can't run tree command do:
either $ brew install tree
or $ port install tree

.
├── README.md
└── platform_simulation
    ├── db.sqlite3
    ├── manage.py
    ├── platform_simulation
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-35.pyc
    │   │   ├── settings.cpython-35.pyc
    │   │   ├── urls.cpython-35.pyc
    │   │   └── wsgi.cpython-35.pyc
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── simulation
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-35.pyc
    │   │   ├── admin.cpython-35.pyc
    │   │   ├── forms.cpython-35.pyc
    │   │   ├── models.cpython-35.pyc
    │   │   ├── urls.cpython-35.pyc
    │   │   └── views.cpython-35.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── file
    │   │   └── AgentTest.csv
    │   ├── forms.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_auto_20170401_1250.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-35.pyc
    │   │       ├── 0002_auto_20170401_1250.cpython-35.pyc
    │   │       └── __init__.cpython-35.pyc
    │   ├── models.py
    │   ├── templates
    │   │   └── simulation
    │   │       ├── index.html
    │   │       └── simulation.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── static
    │   ├── bootstrap
    │   │   ├── css
    │   │   │   ├── bootstrap-theme.css
    │   │   │   ├── bootstrap-theme.css.map
    │   │   │   ├── bootstrap-theme.min.css
    │   │   │   ├── bootstrap-theme.min.css.map
    │   │   │   ├── bootstrap.css
    │   │   │   ├── bootstrap.css.map
    │   │   │   ├── bootstrap.min.css
    │   │   │   └── bootstrap.min.css.map
    │   │   ├── fonts
    │   │   │   ├── glyphicons-halflings-regular.eot
    │   │   │   ├── glyphicons-halflings-regular.svg
    │   │   │   ├── glyphicons-halflings-regular.ttf
    │   │   │   ├── glyphicons-halflings-regular.woff
    │   │   │   └── glyphicons-halflings-regular.woff2
    │   │   └── js
    │   │       ├── bootstrap.js
    │   │       ├── bootstrap.min.js
    │   │       └── npm.js
    │   └── img
    │       └── logoProvidence.png
    └── templates
        └── base.html

17 directories, 52 files





###################
Running the project
###################
In this part, I'll describe all the needed installation and how to run and access the project

$ pip install Django
$ cd platform_simulation/
$ python manage.py runserver --> platform access: http://localhost:8000/





########
Comments
########
Before starting the project, I modify the xslx file into csv without header thanks to pandas librairy and jupyter-notebook

I chose a relational database to store the initial values. 
I defined an abstract model for this data and then a derived model with additional attributes useful to keep track of the simulation
To launch the simulation, the user has to provide the input (brand factor) via an HTML form which sends the value to a view. 
This view gets the value, initialises the database from a CSV file, then launches the simulation. 
When the simulation is finished, it shows the results in the form of simple group bar chart.

It is easy to extend the code to add for another simulation. We can use inheritance, forms, views associated.

To change to dataset, we just have to load another one





#####
Bilan
#####
To realize this mini project I needed to learn a python framework. So I spent time learning Django thanks to this MOOC : 
https://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django/creez-vos-applications-web-avec-django
Then I learned bootstrap, LESS and revised my JS


