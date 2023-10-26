import socket
import subprocess
import psutil
import sys

def lookup(domain_name):
    try:
        return socket.gethostbyname(domain_name)
    except socket.gaierror:
        return None

def ping(ip_address):
    # Pour la compatibilité entre Windows et UNIX (Linux/Mac), nous pourrions avoir besoin d'une petite condition
    parameter = "-n" if sys.platform.lower() == "win32" else "-c"
    response = subprocess.run(['ping', parameter, '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if response.returncode == 0:
        return "UP !"
    else:
        return "DOWN !"

def ip():
    for interface, addresses in psutil.net_if_addrs().items():
        for address in addresses:
            if interface == 'eth0' and address.family.name == 'AF_INET':
                return address.address
    return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("'command' is required as the first argument. Déso.")
        exit()

    command = sys.argv[1]
    if command == "lookup" and len(sys.argv) > 2:
        result = lookup(sys.argv[2])
        if result:
            print(result)
        else:
            print(f"Could not find IP for domain {sys.argv[2]}")
    elif command == "ping" and len(sys.argv) > 2:
        print(ping(sys.argv[2]))
    elif command == "ip":
        result = ip()
        if result:
            print(result)
        else:
            print("Could not find Wi-Fi IP address")
    else:
        print(f"'{command}' is not an available command. Déso.")

