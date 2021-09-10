import paramiko
import ipaddress

def connect(user, ip, password):
    '''
    Функция подключения к оборудованию по SSH
    '''
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=user, password=password, port=22,
                   allow_agent=False, look_for_keys=False)
    return client


def configure_intf(vlan, ip, mask, dhcp=None):
    '''
    Функция генерирует конфигурацию интерфейса
    '''
    conf_t = 'conf t'
    conf_create_vlan = f'vlan {vlan}'
    config_ip_vlan = f'interface vlan {vlan}'
    config_ip = f'ip address {ip} {mask}'
    config_mtu = 'mtu 9216'
    config_dhcp_relay = f'ip dhcp relay address {dhcp}'
    no_shut = 'no shutdown\n'
    if dhcp != None:
       result = [conf_t, conf_create_vlan, config_ip_vlan, config_ip, config_mtu, config_dhcp_relay, no_shut]
    else:
        result = [conf_t, conf_create_vlan, config_ip_vlan, config_ip, config_mtu, no_shut]
    join_result = '\n'.join(result)
    return join_result

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

