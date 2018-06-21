#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import scp
import paramiko


def main():
    while(True):
        time.sleep(5)
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            ssh.connect(hostname='10.144.116.253', port=22, username='pi', password='raspberry')
            with scp.SCPClient(ssh.get_transport()) as scptest:
                scptest.put('alpha.png', '/home/pi/alpha.png')


if __name__ == '__main__':
    main()
