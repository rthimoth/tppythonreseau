from socket import gethostbyname
from sys import argv

domain_name = argv[1]
print(gethostbyname(domain_name))
