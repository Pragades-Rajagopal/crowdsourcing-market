# CROWDSOURCING MARKET APPLICATION

## DEPENDENCIES & START APP
```
sh start_app.sh
```
> Above script will install the dependencies in the system and start the application on default port 8000

## COMMANDS
Commands to create a project, apps within the project, database migration, superusers
```
django-admin startproject <project_name>
```
```
python manage.py runserver  # to test if setup is working for the first time and to start the applications
```
```
python manage.py migrate # to make initial migrations to database
```
```
python manage.py createsuperuser  # to create admin user for the first time
```
```
python manage.py startapp <app_name>   # app name is subset of main project
```
```
python manage.py makemigrations <app_name>   # models in app will be migarted to database

python manage.py migrate
```