import paramiko
import argparse
import sys
import time
from pprint import pprint


def parse_args(argv):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--ip', required=True, help='cloud address')
    parser.add_argument('--password', required=True, help='user password')
    parser.add_argument('--user', required=True, help='username for ssh')
    parser.add_argument('--command', help='command for execute')
    return parser.parse_args(argv)


def connect(user, ip, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=user, password=password, port=22,
                   allow_agent=False, look_for_keys=False)
    return client

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    client = connect(ip=args.ip, user=args.user, password=args.password)
    result = client.invoke_shell()
    result.send(f"{args.command}\n")
    while not result.recv_ready():
        time.sleep(3)
    output = result.recv(60000).decode("utf-8")
    pprint(output, width=120)
    client.close()