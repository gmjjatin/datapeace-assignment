# Datapeace-assignment
Backend Developer Assignment -Jatin. 
This is code repo for an API with which CRUDS ( create ,read ,update , delete , sort ) and filter operations can be performed on the database.

## Video Demonstration
* Installation - https://drive.google.com/file/d/10Xa6OGzw_reh77bT53iV7NjUifiVi8D3/view?usp=sharing
* API demo - https://drive.google.com/file/d/1IF8ZSIOsoqy1Lj5K3tIDKLKAAY5cX304/view?usp=sharing

## Technologies used
* Application Logic - Python
* Framework - Django 
* Database - SQLite3
* UI - Bootstrap , HTML , Jquery , javascript
* Demo data - http://demo9197058.mockable.io/users

## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org/downloads/).
* Open 'terminal' in linux or command prompt in windows .After doing this, confirm that you have installed virtualenv globally as well.If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC . If you don't have git installed follow this [link](https://git-scm.com/).
    ```bash
        $ git clone https://github.com/gmjjatin/datapeace-assignment.git
    ```

* #### Dependencies
    1. Cd into the cloned repo as such:
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
