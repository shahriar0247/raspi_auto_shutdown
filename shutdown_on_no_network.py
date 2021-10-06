#!/usr/bin/python3.7

import socket
import time
import os

def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print("we have internet")
        return True
    except socket.error as ex:
        print("no internet")
        print(ex)
        return False

tried = 0
while True:
    if not internet():
        tried = tried + 1
    else:
        tried = 0
    if tried == 5:
        os.system("shutdown -h now")
    time.sleep(2)

