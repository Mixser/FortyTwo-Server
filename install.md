1. Install pre-requisites
=========================

Virtualenv
----------
Standard installation with virtualevnwrapper.

PostgreSQL
----------
Standard installation.


2. Create virtual environment
=============================

1. Clone repository: ``git clone https://bitbucket.org/razortheory/fortytwo.git``
2. Create virtual environment: ``mkvirtualenv fortytwo``
3. Install requirements ``pip install -r requirements.txt``
4. Edit $VIRTUAL_ENV/bin/postactivate to contain the following lines:

```
export FORTYTWO_ENV=dev
export DATABASE_URL=postgres://<user_name>:<password>@<host>/fortytwo
```

5. Deactivate and re-activate virtualenv:

```
deactivate
workon fortytwo
```

4. Database
=============
1. Create database table:

```
psql -Uyour_psql_user
CREATE DATABASE fortytwo;
```

2. Migrations: ``./manage.py migrate``
3. Create admin: ``./manage.py createsuperuser``
4. Run the server ``./manage.py runserver``


5.Configure heroku app
=====================
To create a new heroku app, run the following command: 
    
    $ heroku create

To push to heroku:

    $ git push heroku master
    
Or set remote to exist app:
    
    $ heroku git:remote -a <application_name>
    
    
To ensure that we have one dyno running the web process type:

    $ heroku ps:scale web=1
    

App requires of the next add-ons:
    
    https://addons.heroku.com/rabbitmq-bigwig (for celery)
    
    https://addons.heroku.com/heroku-postgresql (for database. It's install automatically)
