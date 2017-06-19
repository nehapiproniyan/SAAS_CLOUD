#!/bin/python2

import os,commands,sys,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

os.system('ssh root@192.168.10.121 -X gnome-calculator')

execfile('saas.py')

