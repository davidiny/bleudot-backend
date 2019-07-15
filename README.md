# bleudot-backend

If you encounter a "from exec" error in your manage.py file, do the following.


1. Install and Create a Virtual environment:  python3 -m pip install virtualenv
2. virtualenv venv -p python3 
3. Activate Virtual Environment: source venv/bin/activate 
4. Install Django: pip install django 
5. pip install djangorestframework
6. pip install psycopg2-binary
7. cd to your project and Run Project: cd myproject , python manage.py runserver 
8. You can see your project here : http://127.0.0.1:8000/ 

# To create database
(For More Help Installing Postgres)[https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3]

1. Start psql shell with `psql` command
2. Run `CREATEDB original_database` to create a local database
3. Run `CREATE ROLE admin WITH LOGIN PASSWORD 'admin';` to create a local `admin` role
4. Run `GRANT ALL PRIVILEGES ON DATABASE original_database TO admin;` to grant the `admin` privileges
