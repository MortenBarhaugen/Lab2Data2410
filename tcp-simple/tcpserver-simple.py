from socket import *
def main():
    server_sd = socket(AF_INET, SOCK_STREAM) #Creates a tcp socket on the server
    port = 12000 #Defines the server-port
    server_ip = '127.0.0.1' #Defines the ip of the server

    server_sd.bind((server_ip, port))

    server_sd.listen(1) #Waits for connections

    conn_sd, addr = server_sd.accept() #Waits on accept() for connections

    recieved_line = conn_sd.recv(1024).decode() #Recieves line from client
    print(recieved_line) #Prints recieved line

    #Sends back the recieved line to the client and closes the connection
    conn_sd.send(recieved_line.encode())
    conn_sd.close()
    server_sd.close()

if __name__ == '__main__':
    main()