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
Agradecimento especial Sr. Márcio Albuquerque pela mentória e pacicência.


# API Documentation

route:  index
# Bhub



<!--- If we have only one group/collection, then no need for the "ungrouped" heading -->



## Endpoints

- [Costumer API](#costumer-api)
    - [Dependencies](#dependencies)
    - [How to run this project](#how-to-run-this-project)
    - [Run unit tests](#run-unit-tests)
    - [Create a Mysql Database and configure instance](#create-a-mysql-database-and-configure-instance)
    - [Make migrations](#make-migrations)
    - [Thanks](#thanks)
- [API Documentation](#api-documentation)
- [Bhub](#bhub)
  - [Endpoints](#endpoints)
  - [Clientes](#clientes)
    - [1. cadastrar cliente](#1-cadastrar-cliente)
    - [2. todos clientes](#2-todos-clientes)
    - [3. cliente por id](#3-cliente-por-id)
    - [4. atualizar cliente](#4-atualizar-cliente)
    - [5. deletar cliente](#5-deletar-cliente)
  - [Dados Bancários](#dados-bancários)
    - [1. cadastrar conta](#1-cadastrar-conta)
    - [2. deletar conta](#2-deletar-conta)

--------



## Clientes



### 1. cadastrar cliente



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: http://127.0.0.1:5000/api/v1/clientes/cadastrar
```



***Body:***

```js        
{
    "razao_social": "jose santos",
    "telefone": 31991458907,
    "endereco": "bandolin 13",
    "faturamento_declarado": 10000
}
```



### 2. todos clientes



***Endpoint:***

```bash
Method: GET
Type: 
URL: http://127.0.0.1:5000/api/v1/clientes/consultar
```



### 3. cliente por id



***Endpoint:***

```bash
Method: GET
Type: 
URL: http://127.0.0.1:5000/api/v1/clientes/consultar/1
```



### 4. atualizar cliente



***Endpoint:***

```bash
Method: PUT
Type: RAW
URL: http://127.0.0.1:5000/api/v1/clientes/atualizar/1
```



***Body:***

```js        
{
    "razao_social": "jose santos",
    "telefone": 31991458907
}
```



### 5. deletar cliente



***Endpoint:***

```bash
Method: DELETE
Type: 
URL: http://127.0.0.1:5000/api/v1/clientes/deletar/1
```



## Dados Bancários



### 1. cadastrar conta



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: http://127.0.0.1:5000/api/v1/dadosbancarios/cadastrar
```



***Body:***

```js        
{
    "agencia": "1530",
    "conta": 1045020,
    "banco": 104,
    "id_cliente": 2
}
```



### 2. deletar conta



***Endpoint:***

```bash
Method: DELETE
Type: 
URL: http://127.0.0.1:5000/api/v1/dadosbancarios/deletar/2
```



---
[Back to top](#bhub)

>Generated at 2022-12-06 15:41:04 by [docgen](https://github.com/thedevsaddam/docgen)
