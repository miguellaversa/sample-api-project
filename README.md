# PRGX API

This API provides endpoints for getting, creating, updating, and deleting users and addresses. It is built with Python and FastAPI, uses PostgreSQL as a database, and it is containerized with Docker.

The main components of the API are the controllers, which handle the requests from the client, and the models, which represent the data that is being transferred. The controllers use the models to interact with the database, and the models are used to serialize and deserialize the data in the requests and responses.


<br>
## Prerequisites

Before you get started, you will need to install the Docker and Docker Compose dependencies:

- [Docker](https://www.docker.com/): Latest


<br>
## Getting Started

Once you have installed the dependencies, you can follow these steps to get the API up and running:

1. Clone the repository.
2. In the project directory, run the following command to build the Docker image, create the database and load the sample data:

```
docker-compose up -d
```

After about 2 minutes, the API will be running on port 8000. 

You can interact with the API using tools like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/download). You can also do it using the swagger documentation, which is available at http://localhost:8000/docs


<br>
## Usage

The API works with JWT authentication, in order to start using the API you need to send a request to create the access token, this token will available for 120 minutes. 
This is a user and password previously created to be used in tests, please use it to generate your access token. 

The following is an example of this request:
```
POST http://localhost:8000/login

{
    "username": "prgx",
	"password": "prgx1234"
}
```

The API will return a JSON response with the access token and the token type.

```
{
	"access_token": "token",
	"token_type": "bearer"
}
```


The API provides the following endpoints:

* `GET /users`: Get all users.
* `GET /users/{id}`: Get a single user by ID.
* `GET /users/{country}`: Get all users by country.
* `POST /users`: Create a new user.
* `PUT /users/{id}`: Update a user by ID.
* `DEL /users/{id}`: Delete a user by ID.
* `GET /addresses`: Get all addresses.
* `GET /addresses/{id}`: Get a single address by ID.
* `POST /addresses`: Create a new address.
* `PUT /addresses/{id}`: Update an address by ID.
* `DEL /addresses/{id}`: Delete an address by ID.


This is an example of the body and headers to create a new user

```
data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "password": "password",
    "addresses": []
}

headers = {
    "Authorization": "Bearer " + bearer_token
}
```

For more detailed information, refer to the [API documentation.](http://localhost:8000/docs)


<br>
## Directory Hierarchy

```
|—— .gitignore
|—— api
|    |—— .env
|    |—— config.py
|    |—— controllers
|        |—— auth.py
|        |—— controllers.py
|    |—— database.py
|    |—— main.py
|    |—— middleware
|        |—— get_token.py
|        |—— hashing.py
|        |—— oauth.py
|    |—— models
|        |—— models.py
|    |—— requirements.txt
|    |—— routes
|        |—— auth.py
|        |—— routes.py
|    |—— schemas
|        |—— schemas.py
|—— docker-compose.yml
|—— Dockerfile
|—— sql
|    |—— init.sql
```

<br>
## Sources

- FastAPI documentation: https://fastapi.tiangolo.com/
- PostgreSQL documentation: https://www.postgresql.org/docs/
- Docker documentation: https://docs.docker.com/
