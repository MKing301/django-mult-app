# Django Project w/ Multiple Apps

This project contains the following apps:


* Portfolio - converted Flask app to Django app
* Residential - track home maintenance
* Automotive - track vehicle maintenance

## Resources

* [Ubuntu 20.04](https://releases.ubuntu.com/20.04/)
* [Python3](https://www.python.org/download/releases/3.0/)
* [Pipenv](https://pypi.org/project/pipenv/)
* [Django](https://www.djangoproject.com/)
* [SQLAlchemy - PostgreSQL](http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html)
* [reCAPTCHA](https://www.google.com/recaptcha/about/)
* [Environment Variables](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/)
* [Clone an exising Git repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

## Prerequisite
* Ubuntu 20.04
* Python3
* Clone this repository

*NOTE - If you are on a Windows machine you can use [VirtualBox](https://www.virtualbox.org/) or [WSL](https://docs.microsoft.com/en-us/windows/wsl/about) for Ubuntu*

## Requirements
1. In the django-mult-app directory, type `pipenv shell` to enter virtual the environment
2. Type `pip install -r requirements.txt` to install the required libraries

**TODO** - list environment variables to add to the .bashrc file


## Run the program
1. In the django-mult-app directory, type `pipenv shell` to enter virtual the environment
2. Type `cd project` to enter the project directory
3. Type `python manage.py runserver` to start the development server

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 26, 2021 - 20:27:56
Django version 3.2.8, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
4. Open your browser and access the 3 application at:
  * Portfolio app - [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  * Residential app -  [http://127.0.0.1:8000/residential/](http://127.0.0.1:8000/residential/)
  * Automotive app - [http://127.0.0.1:8000/autos/](http://127.0.0.1:8000/autos/)
