import subprocess
import platform
import socket




def ping(host):
    """
    Use the ping command  for get target ip
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    
    output = subprocess.check_output(command).decode()

    target_ip = output.split(" ")[2]

    if platform.system().lower()=='windows':
        target_ip = target_ip.replace("[","").replace("]","")

    else:
        target_ip = target_ip.replace("(","").replace(")","")

    return(target_ip)