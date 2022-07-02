from pathlib import Path
import sys

ROOT = Path(__file__).parent.parent.resolve()
INTERPRETER = Path(sys.executable)
CADDY_INPUT = Path(ROOT, 'scripts', 'caddy.service')
CADDY_OUTPUT = Path("/etc/systemd/system/caddy.service")
GUNICORN_INPUT = Path(ROOT, 'scripts', 'gunicorn.service')
GUNICORN_OUTPUT = Path("/etc/systemd/system/gunicorn.service")

def write_file():
    gunicorn = GUNICORN_INPUT.read_text()
    gunicorn = gunicorn.replace("$command$", f"{INTERPRETER} -m gunicorn -c {Path(ROOT, 'BE','gunicorn.conf.py')} --chdir {Path(ROOT, 'BE')} django_project.wsgi")
    GUNICORN_OUTPUT.write_text(gunicorn)
    caddy = CADDY_INPUT.read_text()
    caddy = caddy.replace("$command$", f"{Path(ROOT, 'server/caddy')} run --config {Path(ROOT, 'server/Caddyfile')}")
    CADDY_OUTPUT.write_text(caddy)

if __name__ == "__main__":
    write_file()