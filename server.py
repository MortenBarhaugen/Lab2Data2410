"""
Server side: it simultaneously handle multiple clients
and broadcast when a client new client joins or a client
sends a message.
"""
from socket import *
import _thread as thread
import time
import sys

# this is to keep all the newly joined connections!
all_client_connections = []

"""
returns the time of day
"""


def now():
    return time.ctime(time.time())


"""
a client handler function
"""


def handleClient(connection, addr):
    # this is where we broadcast everyone that a new client has joined
    """
    Adds the users to the list and handles them accordingly, it modifies the message and sends it to the
    broadcast function, if the user is new it also boradcasts the message to inform everyone that a new
    user has joined the area
    """

    # append this this to the list for broadcast
    # create a message to inform all other clients
    # that a new client has just joined.

    ### Write your code here ###
    if connection not in all_client_connections:        #checks if the connection is unique
        broadcastMessage = str(addr) + " - Joined the chat" #prepares a message for the other clients with the user id
        all_client_connections.append(connection)       #appends the connection of the new client to the list of active clients

        broadcast(connection, broadcastMessage)         #broadcasts the joining message for the new client to the other clients
    ### Your code ends here ###

    while True:
        message = connection.recv(2048).decode()
        print(now() + " " + str(addr) + "#  ", message)
        if (message == "exit" or not message):
            break
        ### Write your code here ###
        # broadcast this message to the others
        modifiedMessage = str(addr) + str(message) #adds an id to the message so we can differanciate the senders
        broadcast(connection, modifiedMessage)  #broadcasts the message to the other clients
    ### Your code ends here ###
    connection.close()
    all_client_connections.remove(connection)


def broadcast(connection, message):
    """
    The function takes in a string connection that contains the information of the connection of the users,
    it also takes in a modified message that it sends to all the users. it compares all the users logged in with the user
    that sent the message and skips the sender and sends to everyone else.
    """
    print("Broadcasting")
    ### Write your code here ###
    for i in all_client_connections:    #checks all the connections
        if i != connection:             #makes sure we don't send the message to the newly joined user
            i.send(message.encode())    #sends the message to the sockets of one user that is not the newly joined


### Your code ends here ###

def main():
    """
    creates a server socket, listens for new connections,
    and spawns a new thread whenever a new connection join
    """
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    try:
        # Use the bind function wisely!
        ### Write your code here ###
        serverSocket.bind(('', serverPort))     #binds to localhost (internal in the pc) on port 12000
        ### Your code ends here ###

    except:
        print("Bind failed. Error : 1")
        sys.exit()
    serverSocket.listen(10)
    print('The server is ready to receive')
    while True:
        ### Write your code here ###
        connectionSocket, addr = serverSocket.accept()  # accept a connection
        ### You code ends here ###

        print('Server connected by ', addr)
        print('at ', now())
        thread.start_new_thread(handleClient, (connectionSocket, addr))
    serverSocket.close()


if __name__ == '__main__':
    main()
