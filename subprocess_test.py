
import subprocess

folder = 'C:\\Windows\\Temp'
print(f'Trying to delete folder: {folder}')

delete = subprocess.run(f"rmdir /s /q '{folder}'", shell=True)

