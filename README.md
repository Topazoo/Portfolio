# Online Project Portfolio
### Author: Peter Swanson
[![Python 2.7](https://img.shields.io/badge/Python-2.7-brightgreen.svg)](https://www.python.org/downloads/release/python-2714/)
[![Django 1.9.13](https://img.shields.io/badge/Django-1.9.13-brightgreen.svg)](https://pypi.org/project/Django/1.9.13/)


## Background
An online portfolio to showcase some of my personal projects built using the Django Python Web Framework.

## Server Deployment
### Starting the server:
This server can be run on your local machine using Django or deployed to the cloud. For the latter I prefer using:
- An AWS Ubuntu instance (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- Nginx and gunicorn (https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)


The server can be run using <i>manage.py</i>. Note that the server requires two configuration files: <i>praw.ini</i> and <i>server_config.ini</i>
 
 ```
$ ./manage.py runserver
System check identified no issues (0 silenced).
August 10, 2018 - 05:02:18
Django version 1.9.13, using settings 'portfolio.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
 ```

### Create the configuration files:
These file should be placed in the <b>portfolio/</b> directory (the directory that contains 
<i>manage.py</i>).

<i>praw.ini</i> must adhere to the following format: https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html

<i>server_config.ini</i>
```
secret_key=KEY
debug=TRUE/FALSE
hosts=HOSTS
```
Where the right-hand value is your Django secret key, debug setting, and comma seperated host urls (e.g. 127.0.0.1,127.0.0.2) respectively. 

## Files
- portfolio/base/urls.py - URLs that can be visited on the site
- portfolio/base/views.py - Python functions that run when URLs are visited
- portfolio/base/templates/ - HTML templates loaded when URLs are visited
- portfolio/base/static/css/base.css - Style sheet for HTML templates
- portfolio/base/static/js/ - Javascript code
- portfolio/base/Bot.py - Python code for the issue saliency bot demo
- portfolio/base/directory_tree.py - Python code for the Django virtual file hierarchy demo

## Requirements:
Requirements can be fond in <i>requirements.txt</i>. They can be installed via pip.
```
$ pip install -r requirements.txt
```