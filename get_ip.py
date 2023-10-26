import psutil

for interface, addresses in psutil.net_if_addrs().items():
    for address in addresses:
        if interface == 'eth0' and address.family.name == 'AF_INET':  # Assuming the interface is named 'Wi-Fi'. Adjust if needed.
            print(address.address)
            break

