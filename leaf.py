from netmiko import ConnectHandler

# Define the Cumulus switches details
cumulus_devices = [
    {
        'device_type': 'linux',
        'ip': '1.1.1.3',
        'username': 'cumulus',
        'password': 'password',
        'secret': 'password'  # Provide the sudo password for privilege escalation
    },
    {
        'device_type': 'linux',
        'ip': '1.1.1.4',
        'username': 'cumulus',
        'password': 'password',
        'secret': 'password'  # Provide the sudo password for privilege escalation
    },
    {
        'device_type': 'linux',
        'ip': '1.1.1.5',
        'username': 'cumulus',
        'password': 'password',
        'secret': 'password'  # Provide the sudo password for privilege escalation
    },
    {
        'device_type': 'linux',
        'ip': '1.1.1.6',
        'username': 'cumulus',
        'password': 'password',
        'secret': 'password'  # Provide the sudo password for privilege escalation
    }
    # Add more devices as needed
]

# Iterate through each Cumulus switch
for device in cumulus_devices:
    # Connect to the Cumulus switch
    net_connect = ConnectHandler(**device)

    # Configure the hostname and other commands
    config_commands = [
        'net add vlan 10-20'
    ]

    # Send configuration commands
    output = net_connect.send_config_set(config_commands)

    # Commit the changes
    commit_command = 'sudo net commit'
    output += net_connect.send_command(commit_command)

    print(f"Configuration for {device['ip']}:\n{output}")

    # Disconnect from the switch
    net_connect.disconnect()