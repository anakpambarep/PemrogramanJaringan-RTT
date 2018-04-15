#!/usr/bin/python3
# Program RTT Server
# author: erdiansahlan@student.ub.ac.id
# execute: ./code5.1.py 0.0.0.0:8080

import signal
import socket
import sys

srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind(srv_sockaddr)
serversock.listen(1)

print('Listening at', serversock.getsockname())
print("Press Crtl+c to exit...")
while True:
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        datasock, clientsockaddr = serversock.accept()
        print('Client {} connected'.format(clientsockaddr))
        while True:
            data = datasock.recv(2048)
            if data:
                datasock.sendall(data)
            else:
                break
        print('Client {} disconnected'.format(clientsockaddr))
        datasock.close()
    except KeyboardInterrupt:
        break

serversock.close()