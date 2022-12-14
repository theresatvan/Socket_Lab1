# import socket module
from socket import *
import sys  # In order to terminate the program

def webServer(port=6789):
    serverSocket = socket(AF_INET, SOCK_STREAM)  # Prepare a server socket
    
    serverSocket.bind(('', port))  # Bind socket to specified port
    serverSocket.listen(1)  # Server listens for at most 1 TCP connection
    
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # Server accepts a connection and returns a new socket object
        try:
            message = connectionSocket.recv(1024).decode()  # Read bytes from socket
            filename = message.split()[1]
            
            print('Client request \n', message)
            
            f = open(filename[1:])
            outputdata = f.read()  # Retrieve specified file requested from client
            
            # Send one HTTP header line into socket
            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
            
            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
                
            connectionSocket.close()
            
        except IOError:
            # Send response message for file not found
            connectionSocket.send('HTTP/1.1 404 Not found\r\n\r\n'.encode())
            connectionSocket.send('File not found'.encode())
            
            # Close client socket
            connectionSocket.close()
    
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == '__main__':
    webServer(6789)
