# icav

## Download from github

1. Clone this repository in to the system
2. Install the neccesary pyhton packages using requirements.txt
```
pip install requirements.txt
```
## Install postgresql
 1. Create a database using the following command
 ```
 CREATE DATABASE icav;
 ```
## Do migrations
Use the follwing commands for migartions
```
python3 manage.py makemigrations
python3 manage.py migrate
```
## Runserver
Use the following command to runserver

```
python3 manage.py runserver
```

Open in browser http://127.0.0.1:8000/


