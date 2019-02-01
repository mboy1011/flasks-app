# FLASKS-APP
<p><b>FLASKS-APP</b> is a simple web app project using Python3, PostgreSQL, Flask, MaterializeCSS and Heroku as a cloud server. </p>

## Prerequisite:
> * Basic knowledge to Programming (Python).
> * Basic knowledge to RDBMS or SQL Database (MySQL, PostgreSQL).
> * Basic knowledge to Web (HTML, JS, CSS).

## Requirements:
[![Python3](https://www.python.org/static/img/python-logo.png)](https://www.python.org/downloads/)
[![Flask](http://flask.pocoo.org/static/logo.png)](http://flask.pocoo.org/)
[![Heroku](https://www3.assets.heroku.com/assets/logo-purple-08fb38cebb99e3aac5202df018eb337c5be74d5214768c90a8198c97420e4201.svg)](https://www.heroku.com/)

## Installation:
1. Download or Clone this Repository.
2. Create a Python environment:
> * <code>python3 -m venv venv</code>
> * <code>source venv/Scripts/activate</code>
3. Install Python requirements <code>pip3 install -r requirements</code>
4. Export the variable of your database url provided by Heroku Postgres: <code>export DATASEBASE_URL=url
5. Export the flask environment and app: 
    <code>export FLASK_APP=application.py</code>
    <code>export FLASK_ENV=development</code>
6. Create Database on Heroku Postgres: Copy this SQL Code 
    <code>
    CREATE TABLE tbl_employee (
    emp_id SERIAL NOT NULL,
    f_name VARCHAR NOT NULL,
    l_name VARCHAR NOT NULL,
    m_name VARCHAR NOT NULL,
    added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    </code>
    <code>
    CREATE TABLE tbl_users(
    id SERIAL NOT NULL,
    emp_id INTEGER NOT NULL,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    </code>
7. Run the App: <code>flask run</code>

##
[![Compatibility](https://img.shields.io/badge/python-3-brightgreen.svg)](https://github.com/mboy1011/flasks-app.git)