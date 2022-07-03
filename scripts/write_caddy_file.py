import os
from pathlib import Path
from read_env import read_env

ROOT = Path(__file__).parent.parent.resolve()
ENV = Path(ROOT, '.env.json')
CADDY_TMPL = Path(ROOT, 'scripts', 'caddyfile.tmpl')

def write_file(env_path: Path):
    output_path = Path(__file__).parent.parent / Path('server', 'Caddyfile')
    read_env(env_path)
    tmpl = CADDY_TMPL.read_text()
    if os.environ.get("STAGE") == "PRODUCTION":
        tmpl = tmpl.replace('$host$', 'snackeroo.info')
    else:
        tmpl = tmpl.replace('$host$', 'localhost')
    tmpl = tmpl.replace("$root$", str(ROOT))
    output_path.write_text(tmpl)

if __name__ == "__main__":
    write_file(ENV)