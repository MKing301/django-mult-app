# Django Project w/ Multiple Apps

This project contains the following apps:


* Portfolio - converted Flask app to Django app
* Residential - track home maintenance
* Automotive - track vehicle maintenance

## Resources

* [Ubuntu 20.04](https://releases.ubuntu.com/20.04/)
* [Python3](https://www.python.org/download/releases/3.0/)
* [Pip3](https://pip.pypa.io/en/stable/)
* [Pipenv](https://pypi.org/project/pipenv/)
* [Django](https://www.djangoproject.com/)
* [SQLAlchemy - PostgreSQL](http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html)
* [reCAPTCHA](https://www.google.com/recaptcha/about/)
* [Environment Variables](https://dev.to/vladyslavnua/how-to-protect-your-django-secret-and-oauth-keys-53fl)
* [Clone an exising Git repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

## Prerequisite
* Ubuntu 20.04
* Python3
* PostgreSQL
1. Type `sudo apt install postgresql postgresql-contrib` then click `ENTER` key

* Pip3
1. Type `sudo apt-get -y install python3-pip` then click `ENTER` key

* Pipenv
1. Type `sudo apt install pipenv`

*NOTE - If you are on a Windows machine you can use [VirtualBox](https://www.virtualbox.org/) or [WSL](https://docs.microsoft.com/en-us/windows/wsl/about) for Ubuntu*

* Set-up Firewall
1. Install ufw: Type `sudo apt install ufw` then click `ENTER` key
2. Deny incoming traffic: Type `sudo ufw default deny incoming` then click `ENTER` key
3. Allow outgoing traffic: Type `sudo ufw default allow outgoing` then click `ENTER` key
4. Allow http port: Type `sudo ufw allow http` then click `ENTER` key
5. Allow port 8000: Type `sudo ufw allow 8000/tcp` then click `ENTER` key
6. Enable ufw firewall: Type `sudo ufw enable` then click `ENTER` key
7. Verify firewall status: Type `sudo ufw status`

* Set-up Database
1. Type `sudo -u postgres psql postgres` to access postgreSQL
2. Type `\password postgres` to set the password
    1. At prompt, enter 'postgres' as the password
    2. Enter 'postgres' as the password again
3. Type `CREATE DATABASE projectdb;` and then click `ENTER` to create the database
4. Type `q\` then click the `ENTER` key to exit PostgreSQL prompt

* Add Environment Variables
1. Type `cd` then click `ENTER` key
2. Type `sudo nano .bashrc` then click `ENTER` key
3. Add the following lines at the top of the .bashrc file (without the Roman numeral, '.' and space):
    1. export GOOGLE_RECAPTCHA_SITE_KEY="value here"
    2. export GOOGLE_RECAPTCHA_SECRET_KEY="value here"
    3. export EMAIL_HOST_USER ="value here"
    4. export EMAIL_HOST_PASSWORD="value here"
    5. export MAIL_USERNAME="value here"
    6. export MAIL_RECIPIENTS="value here"
4. Click `CTRL + o` then click `ENTER` key to save the update
5. Click `CTRL + x` then click `ENTER` key to exit Nano
6. Type `source .bashrc` for the changes to be applied

* IP Address
1. Type 'ifconfig' to obain IP Address

```
enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.77  netmask 255.255.255.0  broadcast 192.168.1.255
```

2. Add the IP address  reCAPTCHA domains
3. Add the IP Address in the project settings file located in the following directory: `/django-mult-app/project/project`
    1. Add to `ALLOWED_HOSTS = ['192.168.1.77']`

* Clone Repository
1. Type `git clone https://github.com/MKing301/django-mult-app.git` then click `ENTER` key

## Requirements
1. Type `cd django-mult-app` then click `ENTER` key
2. In the django-mult-app directory, type `pipenv shell` to enter virtual the environment
3. Type `pip install -r requirements.txt` to install the required libraries

## Run the program
1. Type `cd project` then click `ENTER` key to enter the project directory
2. Type 'python manage.py makemigrations'  then click `ENTER` key
3. Type 'python manage.py migrate'  then click `ENTER` key
4. Type `python manage.py createsuperuser` then click `ENTER` to create a super user (follow prompts)
4. Type `python manage.py runserver 192.168.1.77:8000` to start the development server (REMEMBER: user your IP Address)

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 26, 2021 - 20:27:56
Django version 3.2.8, using settings 'project.settings'
Starting development server at http://192.168.1.77:8000/
Quit the server with CONTROL-C.
```

5. Open your browser and access the 3 application at:
  * Portfolio app - [http://192.168.1.77:8000/](http://192.168.1.77:8000/)
    1. Landing Page
    2. Add Task
    3. View Log and Edit Task

  * Residential app -  [http://192.168.1.77:8000/residential/](http://192.168.1.77:8000/residential/)
    1. Landing Page
    2. Add Task
    3. View Log and Edit Task

  * Automotive app - [http://192.168.1.77:8000/autos/](http://192.168.1.77:8000/autos/)
    1. Landing Page
    2. Add Service
    3. View Log and Edit Service

6. Open your browser and access the admin page at:
  * Admin page - [http://192.168.1.77:8000/admin/](http://192.168.1.77:8000/admin/)
    1. Add Users
    2. Add Groups
    3. Add Advisors for Automotive app
    4. Add Dealership for Automotive app
    5. Add Service for Automotive app
    6. Add Vehicle for Automotive app
    7. View Contacts for Portfolio app
    8. Add Task for Residential app
    9. Add Vendor for Residential app
