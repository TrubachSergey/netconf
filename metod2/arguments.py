import argparse

def parse_args(argv):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--ip', required=True, help='cloud address')
    parser.add_argument('--password', required=True, help='user password')
    parser.add_argument('--user', required=True, help='username for ssh')
    return parser.parse_args(argv)
