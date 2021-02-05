==============================
Project Management Application
==============================

* `About`_
* `Getting Started`_
* `How to Use?`_

About
-----
This is a small full stack Project Management application. Through the application, a user can create and update projects.  The user can create employees.  Once employees have been created, then those employees can be assigned or unassigned to projects.

Following features are implemented in the application:

1. Full stack web application. Can be run from any browser and perform the required actions.
2. RESTful API's implemented by using Django Rest Framework. For an ease the link to the browsable API's are added in the right side of navbar.
3. Unit Test cases added for (forms, views, urls & models) as a separate module inside the project app.

Link to User Manual: The user manual file **User_Manual.pdf** is present in the root folder itself for reference.

Getting Started
---------------
Assuming that you have Python and ``virtualenv`` installed, set up your environment and install the required dependencies like this or you can install the library using ``pip``:

.. code-block:: sh

    $ git clone https://github.com/Shufyan/project_management.git
    $ cd project_management
    $ virtualenv venv
    ...
    $ . venv/bin/activate
    $ python -m pip install -r requirements.txt

How to Use?
-----------
1. download or Clone the repo to your local system.
2. cd to the directory where requirements.txt is located.
3. activate your virtualenv
4. run: pip install -r requirements.txt in your shell
5. go to the root folder ``project_site`` in this case (you can use any IDE for ease, I prefered VSCode), 
6. run migrations to create database and necessary tables.
7. create a super user by typing ``python manage.py createsuperuser``
8. run the application by typing ``python manage.py runserver``