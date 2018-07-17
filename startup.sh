#!/bin/bash

source venv/bin/activate

if [ $1 == true ] 
then 
    python manage.py runserver 0.0.0.0:4400
fi