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
dev:
	python manage.py collectstatic --noinput
	python manage.py runserver 0.0.0.0:7000
server:
	python manage.py collectstatic --noinput
	python -m gunicorn django_project.wsgi
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
		 -d snackeroo.info \
		 -d www.snackeroo.info \
		 --register-unsafely-without-email \
		 --agree-tos
caddy:
	mkdir -p caddy
	cd caddy
	wget https://github.com/caddyserver/caddy/releases/download/v2.5.1/caddy_2.5.1_linux_amd64.tar.gz -O caddy/caddy.tar.gz
	tar -xvf caddy/caddy.tar.gz --directory=caddy
	python scripts/write_caddy_file.py
	sudo caddy/caddy run --config caddy/Caddyfile