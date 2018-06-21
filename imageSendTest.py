#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import scp
import paramiko

k = paramiko.RSAKey.from_private_key_file("/home/pi/rsa")

def main():
    while(True):
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            #ssh.connect(hostname='10.144.116.253', port=22, username='pi', password='raspberry')
            ssh.connect(hostname = "ec2-13-56-144-143.us-west-1.compute.amazonaws.com", username = "ubuntu", pkey = k)
            with scp.SCPClient(ssh.get_transport()) as scptest:
                print 'ok'
                scptest.put('alpha.png', '~/work/panelx-prototype/panel/src/assets/img/washingmachine-hack/camera/alpha.png')
        time.sleep(5)


if __name__ == '__main__':
    main()
