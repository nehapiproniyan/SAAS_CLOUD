#!/bin/python2

import os,sys,socket,time,commands

x='''
press 1 for firefox:
press 2 for gedit:
press 3 for calculator:
press 4 for screensort:
press 5 for webcam:
press 6 for imageviewer:
press 7 for vlc:
press 8 foe ms office:
'''

print x

ch=raw_input()

if ch == '1' :
	print "wait for firefox"
        execfile('firefox.py')

elif ch == '2' :
	print "wait for a while"
        execfile('gedit.py')


elif ch == '3' :
	print "wait for a while"
        execfile('calculator.py')

elif ch == '4' :
	print "wait for a while"
        execfile('scrnshot.py')

elif ch == '5' :
	print "wait for a while"
        execfile('cheese.py')

elif ch == '6' :
	print "wait for a while"
        execfile('image.py')

elif ch == '7' :
	print "wait for a while"
        execfile('vlc.py')

elif ch == '8' :
	print "wait for a while"
        execfile('ofiice.py')
      
else :
        print "invalid entry"
        print "again choose option"
	execfile('saas.py')

