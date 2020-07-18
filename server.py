#!/usr/bin/python3

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

#Bindin to socket
serversocket.bind((host, port)) #Host will be replaced/substitued with IP, if changed and not running on host

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection
    clientsocket, address = serversocket.accept()

    print("received connection from " % str(address))

    message = 'Thank you for connecting to the server... ya little bitch' + "\r\n"

    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
