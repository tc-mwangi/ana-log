# Analog Task Tracker

An utterly fantastic project starter template for Django 2.0.

## Technologies Used
### Frontend
- HTML5
- CSS
- Bootstrap
- Javascript
- JQuery
- AJAX

### Backend
- Django Web Framework
- Django REST Framework

## How to Install

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pipenv install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.


## License: MIT

## Further Reading

- [Live Site](https://analog-tracker.herokuapp.com/index/)




# TODO list API
### created with django rest framework 

# Description

Vertion 1 of a RESTFul API to create users and tasks. Each user can register and keep track of their own tasks and mark them as complete when they are finished. The user has the posibiltiy to edit the description of the tasks and delete them. The admin can create staff users to check all the tasks.

## Auth system

All the requests made to the API need an **Authorization header** with a valid token and the prefix **Bearer**

```Authorization: Bearer <token>```

In order to obtain a valid token it's necesary to send a request `POST /api/v1/auth/token/` with **username** and **password**. To register a new user it's necesary to make a request `POST /api/v1/users/` with the params:
```
username String
password String
confirm_password String
```

## End Points

### Tasks
* `GET /api/tasks/`
* `POST /api/tasks/`
* `PUT /api/tasks/{pk}`
* `GET /api/tasks/{pk}`
* `PATCH /api/tasks/{pk}`
* `DELETE /api/tasks/{pk}`

## Documentation
All the API docs are available in **http://0.0.0.0:8000/docs/** builded with **Django REST Swagger**

# Installation process 

## Install the system dependencies
* **git** 
* **pip**

## Get the code
* Clone the repository
`git clone https://github.com/spantons/todo_app.git`

## Install the project dependencies

`pip install -r requirements/development.txt`

## Run the command to generate the database
`python manage.py migrate`

## Generate super user
`python manage.py createsuperuser`

## Run the server
`python manage.py runserver` the application will be running on port 8000 **http://0.0.0.0:8000/**

## Run the test
`python manage.py test`
