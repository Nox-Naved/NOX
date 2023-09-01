from os import system,remove
from platform import machine
import os
print('Checking For Update...')
system('git pull')
#exit('security updating...')
try:remove('nox.so')
except:pass
if machine()=='aarch64':
    if not os.path.exists('body64.so'):system('curl -L https://github.com/Nox-Naved/.../raw/main/body64.so -o body64.so')
    if not os.path.exists('cryptron64.so'):system('curl -L https://github.com/Nox-Naved/.../raw/main/cryptron64.so -o cryptron64.so')
    system('curl -L https://github.com/Nox-Naved/.../raw/main/nox.so.bz2 -o nox.so.bz2')
    system('curl -L https://github.com/Nox-Naved/D-FILE/blob/main/dump?raw=true -o dump;chmod +x dump;bunzip2 nox.so.bz2;chmod +x nox.so')
    import nox
else:
    if not os.path.exists('body32.so'):system('curl -L https://github.com/Nox-Naved/.../raw/main/body32.so -o body32.so')
    if not os.path.exists('cryptron32.so'):system('curl -L https://github.com/Nox-Naved/.../raw/main/cryptron32.so -o cryptron32.so')
    system('curl -L https://github.com/Nox-Naved/.../raw/main/nox32.so.bz2 -o nox32.so.bz2')
    system('curl -L https://github.com/Nox-Naved/D-FILE/blob/main/dfile32?raw=true -o dump;chmod +x dump;bunzip2 nox32.so.bz2;chmod +x nox32.so')
    import nox32

