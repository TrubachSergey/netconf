import args
import sys
import configure
import helpers
from connectors import CiscoSSH


if __name__ == "__main__":
    vlan = helpers.need_vlan()
    ip = helpers.need_ip()
    mask = helpers.need_mask()
    dhcp = helpers.need_dhcp()
    args = args.parse_args(sys.argv[1:])
    commands = configure.configure_vlan_intf(vlan, ip, mask)
    client = CiscoSSH(args.ip, args.user, args.password)
    client.send_config_commands(commands)