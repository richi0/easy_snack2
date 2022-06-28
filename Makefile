SHELL := /bin/bash

venv:
	python3 -m venv .venv
install: 
	python -m pip install Django
	python -m pip install python-dotenv
	python -m pip install mailjet-rest
	python -m pip install Pillow
	python -m pip install whitenoise
	python -m pip install django-storages
	python -m pip install boto3
migrate: 
	python manage.py makemigrations
	python manage.py migrate
migrate_media:
	python manage.py migrate_media_to_s3
server: 
	python manage.py collectstatic --noinput
	python manage.py runserver 0.0.0.0:7000
restore:
	python manage.py restore
superuser:
	python manage.py createsuperuser