# Client side connects to the server and sends a message to everyone

import socket
import select
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# write server ip and port, and connect
### write your code here ###
serverName = "127.0.0.1"
serverPort = 12000
client_socket.connect((serverName, serverPort))
### your code ends here ###

while True:

    """ we are going to use a select-based approach here because it will help
    us deal with two inputs (user's input (stdin) and server's messages from socket)
    """
    inputs = [sys.stdin, client_socket]

    """ read the select documentations - You pass select three lists: the 
    first contains all sockets that you might want to try reading; the 
    second all the sockets you might want to try writing to, and the last 
    (normally left empty) those that you want to check for errors. """

    read_sockets, write_socket, error_socket = select.select(inputs, [], [])

    # we check if the message is either coming from your terminal or
    # from a server
    for socks in read_sockets:
        if socks == client_socket:

            # receive message from client and display it on the server side
            # also handle exceptions here if there is no message from the
            # client, you should exit.

            ### write your code here ###
            clientRec = client_socket.recv(2048) #receive the string from server
            if clientRec not in read_sockets:   #check of string already is in the read sockets
                if clientRec.decode() == "" or clientRec.decode() == "exit":    #check if the recieving string is either exit or empty
                    client_socket.close()   #closes the client
                    exit()                  #closes the client
                print(clientRec.decode())            #prints the received content
            ### your code ends here ###

        else:
            # takes inputs from the user
            message = sys.stdin.readline()

            # send a message to the server
            ### write your code here ###
            if message.__contains__("exit") or ''.__eq__(message): #checks if the content put in is either exit or empty to exit
                client_socket.close()       #closes the client
                exit()                      #closes the client

            write_socket.append(message)    #appends the content to the write_socket list to write
            for m in write_socket:          #goes trough every element in write_socket
                client_socket.send(m.encode())      #sends the content of the element m to the server
                write_socket.remove(m)         #removes the earlier message so it doesn't block similar messages to be sent
            ### your code ends here ###


client_socket.close()
