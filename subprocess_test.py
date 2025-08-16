
import subprocess

folder = 'C:\\Windows\\Temp'
print(f'Trying to delete folder: {folder}')

delete = subprocess.run(f"rmdir /s /q '{folder}'", shell=True)

if delete.returncode == 0:
    print("Foldedr deleted successfully.")

else:
    print(f"Failed to delete foldedr. return code: {delete.returncode}")
    
print("\nRunning: sfc /scannow\n")
scan = subprocess.run("sfc /scannow", shell=True)

if scan.returncode == 0:
    print("\n Scan completedd successfully.")

else:
    print(f"Scan failed or foundd issues. Return code: {scan.returncode}")