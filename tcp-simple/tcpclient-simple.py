from socket import *


def main():
    # Assigning the message variable the value "Hello world"
    message = "Hello world"

    # Creating a socket called client_sd. AF_INET represents a string that is (in this case) an IPv4 address.
    # SOCK_STREAM means we are using a TCP connection.
    client_sd = socket(AF_INET, SOCK_STREAM)

    # Defines the ip-address of the server we are connecting to
    server_ip = '127.0.0.1'
    # Defines the port of the connection
    port = 12000

    # Connecting to the server using the server_ip and port variables
    client_sd.connect((server_ip, port))

    # Sending the data that is contained in the message variable
    client_sd.send(message.encode())

    # The message that is received from the server
    recieved_line = client_sd.recv(1024).decode()

    # Prints the received line from the server
    print(recieved_line)

    # Closes the connection
    client_sd.close()


if __name__ == '__main__':
    main()
