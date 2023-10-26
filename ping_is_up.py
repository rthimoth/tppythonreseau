from os import system
from sys import argv

ip_address = argv[1]
response = system(f'ping -c 1 {ip_address}')

if response == 0:
    print("UP !")
else:
    print("DOWN !")
