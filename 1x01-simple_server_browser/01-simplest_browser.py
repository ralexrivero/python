#!/usr/bin/env python
''' Simplest browser '''

import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('127.0.0.1', 80))
cmd = 'GET http://127.0.0.1 HTTP/1.0\r\n\r\n'.encode()
mySock.send(cmd)

while True:
    data = mySock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mySock.close()
