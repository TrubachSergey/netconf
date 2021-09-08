import argparse
import sys
import time
from pprint import pprint

import helpers


def parse_args(argv):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--ip', required=True, help='cloud address')
    parser.add_argument('--password', required=True, help='user password')
    parser.add_argument('--user', required=True, help='username for ssh')
    parser.add_argument('--command', help='command for execute')
    return parser.parse_args(argv)


if __name__ == "__main__":
    vlan = input('Input Vlan number:')
    ip = input('Input IP for vlan:')
    mask = input('Input mask for vlan:')
    config = helpers.configure_intf(vlan=vlan, ip=ip, mask=mask)
    conf_to_str = ''.join(map(str, config))
    args = parse_args(sys.argv[1:])
    client = helpers.connect(ip=args.ip, user=args.user, password=args.password)
    result = client.invoke_shell()
    result.send(f"{conf_to_str}")
    while not result.recv_ready():
        time.sleep(3)
    output = result.recv(60000).decode("utf-8")
    pprint(output, width=120)
    client.close()