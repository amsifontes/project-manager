# [Project Tracker](https://homer-project-manager.herokuapp.com/) 

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)

#### A project timeline visualization tool for architects and contractors

# Guide
---------

### Getting started

* Open the terminal at the top-level directory
* Run the following commands:

```bash
python manage.py migrate
python manage.py runserver
```

You should see the below homepage in the browser:
![Screenshot of Homepage](/readme_images/01_homepage.png)



### Setting Up Your Users

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser



## Relevant Filepaths:

* "urls.py": /homergantt/config/urls.py

* "views.py": /homergantt/project_manager/views.py

* "models.py": /homergantt/project_manager/models.py

* "templates": /homergantt/project_manager/templates/pages/


:License: MIT



Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html
