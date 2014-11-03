Installing Django
=================

To install Django in the new virtual environment, run the following command::

    $ pip install django>=1.7

Creating your project
=====================

To create a new Django project called '**new_project**' using
django-17-heroku, run the following command:
    
    $ git clone https://bitbucket.org/razortheory/django-17-heroku.git

    $ django-admin.py startproject --template=**path to clone of django-17-heroku repo** --extension=py,md,procfile new_project
    
    $ pip install -r requirements.txt
    
    $ ./manange.py syncdb
    
    
Configure heroku app
=====================
App requires of the next add-ons:
    
    https://addons.heroku.com/rabbitmq-bigwig (for celery)
    
    https://addons.heroku.com/heroku-postgresql (for database. It's install automatically)