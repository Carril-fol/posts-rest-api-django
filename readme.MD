<div align="center">

<h1>REST API Posts 🖥️</h1>

</div>

### This REST API provides operations for managing posts, comments, and profiles.

## Technologies

<div align="center">

![Static Badge](https://img.shields.io/badge/python-3.10.11-yellow?style=flat-square&logo=python&color=%23f7e185)

![Static Badge](https://img.shields.io/badge/django-4.2.4-greenlight?style=flat-square&logo=django&color=%2342b883)

![Static Badge](https://img.shields.io/badge/django_rest_framework-3.14.0-yellow?style=flat-square&logo=django%20rest%20framework&color=%23f95959)

</div>

## Table of content 📋

* ### [Instalation](#installation)
* ### [Configuration](#configuration)

## Features

### Posts:

* #### Create a Post: Allows users to create a new post with title, description and tags.
* #### List Posts: Retrieves a list of available Posts.
* #### View a Post: Displays the details of a specific Post, including its title, description, and author.
* #### Update a Post: Allows users to modify their own existing post.
* #### Delete a Post: Allows users to delete their own post.
* #### Like a Post: Allows users to indicate if they like a Post.

### Comments:

* #### Add a Comment: Allows users to add comments to a Post.
* #### View Comments: Retrieves the comments associated with a specific Post.
* #### Like Comments: Allows users to like a comment.
* #### Delete Comments: Allows the user to delete his comments from the Posts if he wants to do so.

### Profiles:
        
* #### Create a Profile: User profiles are created automatically when they register.
* #### Update a Profile: Allows users to update their profile
* #### Follow Profiles: Allows other users to follow Profiles of other users.

## Installation

#### To install this repository:

```
In the IDLE terminal:

> git clone https://github.com/Carril-fol/task-management-django-rest.git
```

## Configuration

#### Once installed, you have to configure the database in the project's settings.py:

>**Note:**
> This API uses MYSQL as default, you change what you think needs to change.

#### Add the following fields: NAME, USER, PASSOWORD from your database.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '', 
        'PORT': '',
    }
}
```

#### Once you add the above fields:

````
In the IDLE terminal:

> py manage.py makemigrations

> py manage.py migrate
````````

## Launch

> **Note:**
> Since it is a REST API, it can be consulted from an external program that allows it or from a frontend application.

#### How do I check my Python version:

````
In the IDLE terminal:
> py --version
> Python 3.10.11

In Windows CMD:
c:\> py --version
c:\> Python 3.10.11
``````

#### Install Dependencies:

#### To install the dependencies you need to run 'pip install', make sure you are in the project folder and there you should be able to see the 'requirements.txt' file:

```
In the IDLE terminal:
> pip install -r requirements.txt
```

#### Start the server:

```
In the IDLE terminal:
> py manage.py runserver
````

## Frontend Connection 

#### To make the connection with the backend in the frontend, it is necessary to perform a few steps:

#### What you have to do is to add in settings.py add the URL in 'CORS_ALLOWED_ORIGINS', between single or double quotes.

#### For example:

````
CORS_ALLOWED_ORIGINS = [
     "http://localhost:3000"
]
````
#### With that, it is already configured in the backend for you to use it as you wish. Now you would have to configure how you send the requests from the frontend you are using.