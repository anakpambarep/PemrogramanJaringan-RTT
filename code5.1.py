#!/usr/bin/python3
# Program RTT Server
# author: erdiansahlan@student.ub.ac.id
# execute: ./code5.1.py 0.0.0.0:8080

import sys
import socket
import signal

srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind(srv_sockaddr)
serversock.listen(1)

print('Listening at', serversock.getsockname())
print("Press Crtl+c to exit...")
while True:
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        datasock, clientsockaddr = serversock.accept()
        for _ in range(10):
            datasock.sendall(datasock.recv(2048))
        datasock.close()
    except KeyboardInterrupt:
        break
serversock.close()