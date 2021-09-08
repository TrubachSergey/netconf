import paramiko

def connect(user, ip, password):
    '''
    Функция подключения к оборудованию по SSH
    '''
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=user, password=password, port=22,
                   allow_agent=False, look_for_keys=False)
    return client


def configure_intf(vlan, ip, mask):
    '''
    Функция генерирует конфигурацию интерфейса
    '''
    conf_t = 'conf t\n'
    conf_create_vlan = f'vlan {vlan}\n'
    config_ip_vlan = f'interface vlan {vlan}\n'
    config_ip = f'ip address {ip} {mask}\n'
    config_mtu = 'mtu 9216\n'
    no_shut = 'no shutdown\n'
    result = [conf_t, conf_create_vlan, config_ip_vlan, config_ip, config_mtu, no_shut]
    return result


