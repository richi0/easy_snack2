import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ENV = Path(BASE_DIR, ".env.json")

if ENV.exists():
    env = json.loads(ENV.read_bytes())
    for item in env.items():
        os.environ.setdefault(item[0], item[1])

bind = "127.0.0.1:8001"
workers = 4
accesslog = "-"

if os.environ.get("PRODUCTION") == "True":
    bind = "127.0.0.1:443"
    keyfile = "private.key"
    certfile = "selfsigned.crt"
