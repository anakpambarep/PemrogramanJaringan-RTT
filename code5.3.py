#!/usr/bin/python3
# Program RTT Server Multithread
# author: erdiansahlan@student.ub.ac.id
# execute: ./code5.3.py 0.0.0.0:8080

import signal
import socket
import sys
import threading

class Client(threading.Thread):
    def __init__(self, datasock):
        threading.Thread.__init__(self)
        self.datasock = datasock

    def run(self):
        for _ in range(10):
            self.datasock.sendall(self.datasock.recv(2048))
        print('Client {} disconnected'.format(self.datasock.getpeername()))
        self.datasock.close()

srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind(srv_sockaddr)
serversock.listen(1)
clientthreaddict = {}

print('Listening at', serversock.getsockname())
print("Press Crtl+c to exit...")
while True:
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        datasock, clientsockaddr = serversock.accept()
        print('Client {} connected'.format(clientsockaddr))
        clientthread = Client(datasock)
        clientthreaddict[clientsockaddr] = clientthread
        clientthread.start()
    except KeyboardInterrupt:
        print("Waiting client threads...")
        for clientthread in clientthreaddict.values():
            clientthread.join()
        break

serversock.close()