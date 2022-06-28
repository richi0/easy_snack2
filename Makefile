SHELL := /bin/bash

venv:
	source .venv/bin/activate
install:
	python3 -m venv .venv
	source .venv/bin/activate
	python -m pip install Django
	python -m pip install python-dotenv
	python -m pip install mailjet-rest
	python -m pip install Pillow
	python -m pip install whitenoise
migrate: venv
	python manage.py makemigrations
	python manage.py migrate
server: venv
	python manage.py runserver 0.0.0.0:7000
restore:
	python manage.py restore