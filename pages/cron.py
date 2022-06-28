from django.core import management

def upload_backup():
	management.call_command("backup")