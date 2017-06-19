#!/bin/python2

import os,commands,sys,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

os.system('ssh root@192.168.10.121 -X libreoffice4.3')

execfile('saas.py')

