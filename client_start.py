#!/usr/bin/python2

import  socket,os,commands,time,sys,getpass

sip="192.168.10.121"
sport=1234

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# telnet  server  username  
user=raw_input("enter  user name :  ")
# telnet server password
password=getpass.getpass("enter  user password  :  ")


s.sendto(user,(sip,sport))
s.sendto(password,(sip,sport))

u=s.recvfrom(100)

print u
  
x='''
press 1 for software as a service
'''
print x

ch=raw_input()
if ch == '1' :
	print "wait for a while"

time.sleep(2)
 
execfile('saas.py')

 
