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
    gunicorn = gunicorn.replace("$command$", f"{INTERPRETER} -m gunicorn django_project.wsgi")
    print(gunicorn)
    GUNICORN_OUTPUT.write_text(gunicorn)
    caddy = CADDY_INPUT.read_text()
    caddy = caddy.replace("$command$", f"{Path(ROOT, 'caddy/caddy')} run --config {Path(ROOT, 'caddy/Caddyfile')}")
    CADDY_OUTPUT.write_text(caddy)
    print(caddy)

if __name__ == "__main__":
    write_file()