import ipaddress

def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as err:
        return False

def need_ip():
    ip = input('Input IP for vlan:')
    if check_ip(ip) == True:
        return ip
    else:
        print('Invalid IP address, please try again')
        need_ip()

def need_mask():
    mask = input('Input mask for vlan ip:')
    ip = mask
    if check_ip(ip) == True:
        return mask
    else:
        print('Invalid mask address, please try again')
        need_mask()

def need_dhcp():
    is_dhcp = input('Do you need DHCP relay? (Yes or No):')
    if is_dhcp.lower() == 'yes':
        dhcp = input('Input DHCP relay address:')
        ip = dhcp
        if check_ip(ip) == True:
            return dhcp
        else:
            print('Invalid IP address, please try again')
            need_dhcp()

def need_vlan():
    vlan = int(input('Input Vlan number:'))
    if vlan >= 1 and vlan < 4095:
        return vlan
    else:
        print('Invalid VLAN number, please try again')
        need_vlan()

def need_port():
    port = int(input('Input port number for configure:'))
    if port >= 1 and port <= 52
        return port
    else:
        print('Port is not in range, please try again')
        need_port()