#!/bin/bash
source venv/bin/activate
source .env

if [[ $1 == true ]]
then 
    python manage.py runserver 0.0.0.0:4400
elif [[ $1 == "mg" ]]
then 
    python manage.py migrate
elif [[ $1 == "mkmg" ]]
then 
    python manage.py makemigrations
fi