#!/usr/bin/python2


import  socket,os,commands,time,sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("192.168.10.121 ",1234))

data=s.recvfrom(100)
data1=s.recvfrom(100)

if  data[0] == 'root' and  data1[0]  ==  'q'  :
	s.sendto("ok",data[1])

else :
	
	exit()
