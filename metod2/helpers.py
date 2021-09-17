import ipaddress


def check_answer(answer):
    if answer == 'yes':
        return True
    else:
        return False

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
    if check_ip(mask) == True:
        return mask
    else:
        print('Invalid mask address, please try again')
        need_mask()

def need_dhcp():
    is_dhcp = input('Do you need DHCP relay? (Yes or No):').lower().strip()
    if check_answer(is_dhcp) == True:
        dhcp = input('Input DHCP relay address:')
        if check_ip(dhcp) == True:
            return dhcp
        else:
            print('Invalid IP address, please try again')
            return need_dhcp()

def need_vlan():
    vlan = int(input('Input Vlan number:'))
    if 1 <= vlan < 4095:
        return vlan
    else:
        print('Invalid VLAN number, please try again')
        need_vlan()

def need_port():
    port = int(input('Input port number for configure:'))
    if 1 <= port < 52:
        return port
    else:
        print('Port is not in range, please try again')
        need_port()

def need_trunk():
    trunk = input('Do you want to configure trunk? (Yes or No):').lower().strip()
    if check_answer(trunk) == True:
        return trunk




