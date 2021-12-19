#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '0.0.0.0' #choose IP of server


port = 1234 #set the same port which was on server script

clientsocket.connect((host, port))

message = clientsocket.recv(1024) #max data 

clientsocket.close()

print(message.decode('ascii'))