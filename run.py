from os import system,remove
from platform import machine
print('Checking For Update...')
system('git pull')
try:remove('nox')
except:pass
if machine()=='aarch64':
    system('curl -L https://github.com/Nox-Naved/.../raw/main/nox -o nox')
    system('curl -L https://github.com/Nox-Naved/D-FILE/blob/main/dfile?raw=true -o dump;chmod +x nox;./nox')
else:
    system('curl -L https://github.com/Nox-Naved/.../raw/main/nox32 -o nox')
    system('curl -L https://github.com/Nox-Naved/D-FILE/blob/main/dfile32?raw=true -o dump;chmod +x nox;./nox')
system('clear')
