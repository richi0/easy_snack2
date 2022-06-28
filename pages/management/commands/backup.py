import base64
import datetime
import os
import shutil
from pathlib import Path
import tarfile

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand
import requests

root = Path(__file__).parent.resolve()
temp_folder = Path(root, "temp")
temp_mediafiles = Path(temp_folder, "mediafiles")
project_root = root.parent.parent.parent
mediafiles = Path(project_root, "mediafiles")


class Command(BaseCommand):
    help = "Creates a backup of db and media files and saves it on Dropbox"
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    bu_file = Path(temp_folder, f"{date_time}_db_backup.json")

    def create_temp_folder(self):
        temp_folder.mkdir(exist_ok=True)

    def remove_temp_folder(self):
        shutil.rmtree(temp_folder)

    def copy_media_files(self):
        shutil.copytree(mediafiles, temp_mediafiles, dirs_exist_ok=True)

    def create_tar_file(self) -> Path:
        tar_name = Path(temp_folder, f"{self.date_time}_backup.tar")
        tar = tarfile.open(tar_name, "w:xz")
        all_files = temp_folder.rglob("*.*")
        for name in all_files:
            tar.add(name, arcname=Path(str(name)[len(str(temp_folder)) :]))
        tar.close()
        return tar_name

    def upload_file(self, tar_file: Path):
        url = os.getenv("BACKUP_URL")
        password = os.getenv("BACKUP_PASSWORD")
        auth = requests.post(f"{url}login", json={"password": password})
        cookie = auth.cookies.get("auth")
        f = base64.b64encode(tar_file.read_bytes()).decode('ascii')
        data = {"path": f"backup/{tar_file.name}", "data": f}
        req = requests.post(f"{url}upload", cookies={"auth": cookie}, json=data)
        print(req.content)


    def handle(self, *args, **options):
        if temp_folder.exists():
            shutil.rmtree(temp_folder)
        if settings.DEBUG:
            print(
                f"{self.date_time} No backup created because Django runs in debug mode"
            )
        else:
            self.create_temp_folder()
            with open(self.bu_file, "w") as f:
                management.call_command("dumpdata", stdout=f)
            self.copy_media_files()
            tar_name = self.create_tar_file()
            self.upload_file(Path(temp_folder, tar_name))
            self.remove_temp_folder()
            print(f"{self.date_time} Created backup and uploaded to simpleFileServer")
