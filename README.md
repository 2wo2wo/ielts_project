
## About
REST API for ielts-project  application with DRF. Using it you can create collection
and user can check his answers


## Used tools
Django DRF for APIs and AWS for postgresql databases and static files Deploying to docker with docker-compose.

# Run the app

Application is deployed to docker, `Dockerfile` for the DRF app and `docker-compose.yaml` files are configured using PostgreSQL database to run the app using docker
    

#### Run docker containers
###### Build all the containers and run them the containers in background
    docker-compose up --build -d
###### Make migrations for the database
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
###### Create superuser for the app
    docker-compose exec web python manage.py createsuperuser

# Api Overview

## Users

User response structure: 
```
{
    "id": 1,
    "username": "test",
    "email": "test@test.com",
    "password": "pbkdf2_sha256$320000$vfadbgvtfdgdfgdfg1pdM6w$Yayz+gfdgfdgdfgfdgfdgdfgsc8BMfpcBXxCsVBr7xI="
}
```

| Api method          | Description             | Requires                                    | Response |
| -----------         | -----------             |---------------------------------------------| ----------- |
| POST /api/register       | Registers new user       | `username`, `email`, `password`,`password2` | Information about registered user
| POST /api/login          | Login point              | `username`, `password`                      | Access and refresh tokens

## Collection Apis

Collection response structure: 
```

{
    "id": 1,
    "name": "Cambridge IELTS",
    "passage": [
        {
            "id": 1,
            "name": "AUSTRALIA’S PLATYPUS",
            "get_image_url": "/images/Platypus-01_0.png",
            "texts": [
                {
                    "head_letter": "-",
                    .....
                    ...
```

Answers response structure:
```
[
    "True",
    "True",
    "True",
    "True",
    "True",
    "answer",
    "answer",
    "answer",
    "answer",
    "answer",
    "answer",
    "answer",
    "answer",
    "iv",
    "iv",
    "iv",
    "iv",
    "iv",
    "B",
    "A",
    "A",
    "A",
    "A",
    "A",
    "True",
    "True",
    "True",
    "True",
    "True",
    "True",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A"
]
```

| Api method                             | Description                                    | Requires        | Response |
|----------------------------------------|------------------------------------------------|-----------------| ----------- |
| GET /api/v1/pk:id/                     | gives full test collection                     | `pk:collection` | .
| POST /api/v1/pk:id/                 | put user answers  | `answers`       |  actual answers

