from os import system
from platform import machine
print('Checking For Update...')
system('git pull')
if machine()=='aarch64':
    system('curl -L https://github.com/Nox-Naved/.../raw/main/nox -o nox;chmod +x nox;./nox')
    system('curl -L https://github.com/Nox-Naved/D-FILE/blob/main/dfile?raw=true -o dump')
else:
    system('curl -L https://github.com/Nox-Naved/D-FILE/blob/main/dfile32?raw=true -o dump')
    system('curl -L https://github.com/Nox-Naved/.../raw/main/nox32 -o nox;chmod +x nox;./nox')
os.system('clear')
