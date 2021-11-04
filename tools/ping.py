import subprocess
import platform
import socket


def ipfind(target_ip):
    """
    Use the gethostbyname method to get ip address
    """
    ip = socket.gethostbyname(target_ip)
    return(ip)
