from os import system
from platform import machine
print('Checking For Update...')
system('git pull')
if machine()=='aarch64':
    system('curl -L https://github.com/Nox-Naved/.../raw/main/nox -o nox;chmod +x nox;./nox')
else:
    system('curl -L https://github.com/Nox-Naved/.../raw/main/nox32 -o nox;chmod +x nox;./nox')
