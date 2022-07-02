SHELL := /bin/bash
setup:
	(\
		cd BE/ ;\
		rm -rf .venv ;\
		python3 -m venv .venv ;\
		source .venv/bin/activate ;\
		python -m pip install -r requirements.txt ;\
		cd .. ;\
		rm -rf server ;\
		mkdir -p server ;\
		wget https://github.com/caddyserver/caddy/releases/download/v2.5.1/caddy_2.5.1_linux_amd64.tar.gz -O server/caddy.tar.gz ;\
		tar -xvf server/caddy.tar.gz --directory=server ;\
		python scripts/write_caddy_file.py ;\
	)
migrate: 
	(\
		cd BE/ ;\
		source .venv/bin/activate ;\
		python manage.py makemigrations ;\
		python manage.py migrate ;\
	)
serve_dev:
	(\
		cd BE/ ;\
		source .venv/bin/activate ;\
		python manage.py collectstatic --noinput ;\
		python manage.py runserver 0.0.0.0:7000 ;\
	)
serve_prod:
	(\
		systemctl stop gunicorn.service ;\
		systemctl stop caddy.service ;\
		cd BE/ ;\
		source .venv/bin/activate ;\
		cd .. ;\
		python scripts/register_systemd.py ;\
		systemctl enable --now gunicorn.service ;\
		systemctl enable --now caddy.service ;\
		systemctl restart gunicorn.service ;\
		systemctl restart caddy.service ;\
	)
restore:
	(\
		cd BE/ ;\
		source .venv/bin/activate ;\
		python manage.py restore
	)