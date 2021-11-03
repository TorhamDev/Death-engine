import subprocess
import platform  
import socket

def ping_clear(ping_output):
    """
    clear ping function output and return ip 
    """
    if platform.system().lower()=='windows': 
        ip = ping_output.split(" ")[2].replace("[","").replace("]","") 
    else:
        ip = ping_output.split(" ")[2].replace("(","").replace(")","")

    return ip

def ping(host):
    """
    Use the ping command  for get target ip
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    return ping_clear(subprocess.check_output(command).decode())
