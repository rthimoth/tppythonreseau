from os import system
from sys import argv

ip_address = argv[1]
system(f'ping {ip_address}')