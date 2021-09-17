import sys
import helpers
from arguments import parse_args
from connectors import CiscoSSH


def configure_vlan_intf(vlan, ip, mask, dhcp=None):
    '''
    Функция создает и настраивает интерфейс vlan
    '''
    conf_create_vlan = f'vlan {vlan}'
    config_ip_vlan = f'interface vlan {vlan}'
    config_ip = f'ip address {ip} {mask}'
    config_mtu = 'mtu 9216'
    config_dhcp_relay = f'ip dhcp relay address {dhcp}'
    no_shut = 'no shutdown\n'
    if dhcp != None:
       result = [conf_create_vlan, config_ip_vlan, config_ip, config_mtu, config_dhcp_relay, no_shut]
    else:
        result = [conf_create_vlan, config_ip_vlan, config_ip, config_mtu, no_shut]
    return result

def configure_phisical_intf(port, vlan=None, trunk=None):
    '''
    Функция настраивает физический интерфейс)
    '''
    conf_port = f'interface eth1/{port}'
    conf_access = 'switchport mode access'
    conf_trunk = 'switchport mode trunk'
    conf_vlan = f'switchport access {vlan}'
    if trunk != None:
        result = [conf_port, conf_trunk]
    else:
        result = [conf_port, conf_access, conf_vlan]
    return result

def cisco_create_vlan():
    '''
    Функция запрашивает у пользователя данные для
    создания vlan
    :return:
    '''
    vlan = helpers.need_vlan()
    ip = helpers.need_ip()
    mask = helpers.need_mask()
    dhcp = helpers.need_dhcp()
    args = parse_args(sys.argv[1:])
    commands = configure_vlan_intf(vlan, ip, mask, dhcp)
    client = CiscoSSH(args.ip, args.user, args.password)
    client.send_config_commands(commands)

def cisco_phisical_intf():
    '''
    Функция запрашивает у пользователя данные для
    пеервода физического интерфейса в необходимый режим
    :return:
    '''
    vlan = helpers.need_vlan()
    port = helpers.need_port()
    trunk = helpers.need_trunk()
    print(trunk)
    args = parse_args(sys.argv[1:])
    commands = configure_phisical_intf(port, vlan, trunk)
    client = CiscoSSH(args.ip, args.user, args.password)
    client.send_config_commands(commands)