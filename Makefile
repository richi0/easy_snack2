SHELL := /bin/bash

venv: clean
	python3 -m venv .venv
install: 
	python -m pip install -r requirements.txt
migrate: 
	python manage.py makemigrations
	python manage.py migrate
migrate_media:
	python manage.py migrate_media_to_s3
dev: static
	python manage.py runserver 0.0.0.0:7000
server: static
	python -m gunicorn django_project.wsgi
static:
	python manage.py collectstatic --noinput
restore:
	python manage.py restore
superuser:
	python manage.py createsuperuser
clean:
	rm -rf .venv
cert:
	sudo .venv/bin/certbot certonly \
		 --standalone \
		 --preferred-challenges http \
		 -d example.com \
		 --register-unsafely-without-email \
		 --agree-tos