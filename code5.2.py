#!/usr/bin/python3
# Program RTT client
# author: erdiansahlan@student.ub.ac.id
# execute: ./code5.2.py 127.0.0.1:8080 100

import socket
import sys
import time

srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
count = int(sys.argv[2])
payload = b'x' * 1024

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect(srv_sockaddr)

print('Client has been assigned socket name', clientsock.getsockname())
totalRTT = 0

for i in range(0, count):
    sendtime = time.time()
    clientsock.send(payload)
    reply = clientsock.recv(2048)
    RTT = time.time() - sendtime
    print("Packet {0:d} RTT {1:.5f} s".format(i, RTT))
    totalRTT += RTT
    time.sleep(1)

clientsock.close()
print("RTT average: {0:.5f} s".format(totalRTT / count))