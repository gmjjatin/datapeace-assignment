# Datapeace-assignment
Backend Developer Assignment -Jatin. 
This is code repo for an API with which CRUDS ( create ,read ,update , delete , sort ) and filter operations can be performed on the database.

## Video Demonstration

## Technologies used
* Application Logic - Python
* Framework - Django 
* Database - SQLite3
* UI - Bootstrap

## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/gmjjatin/datapeace-assignment.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd datapeace-assignment
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the api service on your browser by using
    ```
        http://localhost:8000/api/user
    ```
