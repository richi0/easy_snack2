import json
import os
from pathlib import Path

def read_env(file: Path):
    if file.exists():
        env = json.loads(file.read_bytes())
        for item in env.items():
            os.environ.setdefault(item[0], item[1])
    else:
        print(f"Cannot find env file {file}")
        os.abort()
