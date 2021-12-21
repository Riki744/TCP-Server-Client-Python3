#!/usr/bin/python3

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #communication types

#host = Server IP
host = "0.0.0.0"
port = 1234 #port to listen on choose any port you like 

print("Server with IP", host ,"is listening on port", port)

#Binding to socket
serversocket.bind((host, port)) #Host will be replaced with IP

#setup listener TCP with ammount how much it can listen
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept() #starting connection
    print("Received connection from %s " % str(address))

    messsage = 'Hello! Thank you for connecting to the server. This is an example how sockets can be used' + "\r\n" #message on client
    clientsocket.send(messsage.encode('ascii'))

    clientsocket.close()
