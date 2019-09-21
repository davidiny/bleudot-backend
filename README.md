# bleudot-backend

## Git Branching Model

Our branching model is inspired from [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/).

In essence, we will have the following branches:
1. **master**: meant for deployment
2. **develop**: meant for merging in new feature branches
3. **feature(s)**: meant for developing individual features

In the initial stages of development, we'll follow this simple model with two main branches (master and develop), and as many additional feature branches as needed. As complexity and stability increase, we can add release and hotfix branches (as explained in [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/))


## Setting up a virtual environment
If you encounter a "from exec" error in your manage.py file, do the following:  

1. Install and Create a Virtual environment:  python3 -m pip install virtualenv
2. virtualenv venv -p python3 
3. Activate Virtual Environment: source venv/bin/activate 
4. Install Django: pip install django 
5. pip install djangorestframework
6. pip install psycopg2-binary
7. cd to your project and Run Project: cd myproject , python manage.py runserver 
8. You can see your project here : http://127.0.0.1:8000/ 

# To create database
[For More Help Installing Postgres](https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3)

1. Start psql shell with `psql` command
2. Run `CREATEDB original_database` to create a local database
3. Run `CREATE ROLE admin WITH LOGIN PASSWORD 'admin';` to create a local `admin` role
4. Run `GRANT ALL PRIVILEGES ON DATABASE original_database TO admin;` to grant the `admin` privileges

# File Structure

Files in bluedot_backend should only be ones that will be used by all apps, such as urls.py
Files specific to applications will be inside their own application (eg. serializers for the models found in main_calendar will be found in the main_calendar directory
