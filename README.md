# Costumer API
- Teste técnico para organização Bhub

### Dependencies
- Flask
- SQLAlchemy
- Flask Migrate
- SQLite
- Marshmallow
- Pytest

### How to run this project
```sh
pip install pipenv
pipenv install -r requirements.txt
export FLASK_APP=app
export FLASK_DEBUG=1
pipenv shell
flask run
```

# API Documentation

route:  /api/v1/docs

### Run unit tests
```sh
pytest
```
### Create a Mysql Database and configure instance
- on project directory directiory
```sh
mkdir instance
cd instance
touch config.py
```
- Config your db instance in config.py file
```sh
local_host = 'db_host_name'
local_user = 'user_name'
local_password = 'password'
local_db = 'database_name'
```


### Make migrations
```sh
flask db init
flask db migrate
flask db upgrade
```

### Thanks
Agradecimento especial Sr. Marcio pela mentória e pacicência.
