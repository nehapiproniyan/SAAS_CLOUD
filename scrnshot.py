
import os,commands,sys,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

os.system('ssh -X root@192.168.10.121  gnome-screenshot')

execfile('saas.py')

