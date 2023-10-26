from os import system
from sys import argv

ip_address = argv[1]
system(f'ping -c 4 {ip_address}')

