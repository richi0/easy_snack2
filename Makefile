SHELL := /bin/bash
setup:
	(\
		rm -rf .venv ;\
		python3 -m venv .venv ;\
		source .venv/bin/activate ;\
		python -m pip install -r requirements.txt ;\
		rm -rf caddy ;\
		mkdir -p caddy ;\
		wget https://github.com/caddyserver/caddy/releases/download/v2.5.1/caddy_2.5.1_linux_amd64.tar.gz -O caddy/caddy.tar.gz ;\
		tar -xvf caddy/caddy.tar.gz --directory=caddy ;\
		python scripts/write_caddy_file.py ;\
	)
migrate: 
	python manage.py makemigrations
	python manage.py migrate
serve_dev:
	(\
		source .venv/bin/activate ;\
		python manage.py collectstatic --noinput ;\
		python manage.py runserver 0.0.0.0:7000 ;\
	)
serve_prod:
	(\
		source .venv/bin/activate ;\
		python scripts/register_systemd.py ;\
		systemctl enable --now gunicorn.service ;\
		systemctl enable --now caddy.service ;\
		systemctl status gunicorn.service ;\
		systemctl status caddy.service ;\
	)
restore:
	python manage.py restore