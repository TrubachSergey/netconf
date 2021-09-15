import configure

if __name__ == "__main__":
    while True:
        conf_choose = int(input("Do you want to:\n "
        "1) Configure port\n "
        "2) Create and configure vlan\n "))
        # check if conf_choose is equal to one of the strings, specified in the list
        if conf_choose in [1, 2]:
            # if it was equal - break from the while loop
            break
    # process the input
    if conf_choose == 1:
        configure.cisco_phisical_intf()
    elif conf_choose == 2:
        configure.cisco_create_vlan()
