import argparse
import sys
import time
import helpers
from pprint import pprint

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
    ip = helpers.need_ip()
    mask = helpers.need_mask()
    config = helpers.configure_intf(vlan=vlan, ip=ip, mask=mask)
    args = parse_args(sys.argv[1:])
    client = helpers.connect(ip=args.ip, user=args.user, password=args.password)
    result = client.invoke_shell()
    result.send(config)
    while not result.recv_ready():
        time.sleep(3)
    client.close()