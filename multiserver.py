# import socket module
from socket import *
from threading import * # In order to create threads
import sys  # In order to terminate the program

def webServer(port=6789):
    serverSocket = socket(AF_INET, SOCK_STREAM)  # Prepare a server socket
    
    serverSocket.bind(('', port))  # Bind socket to specified port
    serverSocket.listen(5)  # Server listens for at most 5 TCP connection
    
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # Server accepts a connection and returns a new socket object
        
        # Create new thread
        thread = Thread(target=sendResponse, args=(connectionSocket, addr))
        thread.start()
    
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data
    
def sendResponse(connection, address):
    try:
        message = connection.recv(1024).decode()    # Read bytes from socket
        filename = message.split()[1]
        
        print('[thread] client', address, 'request', filename)
        
        f = open(filename[1:])
        outputData = f.read()   # Retrieve specified file requested from client
        
        connection.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        
        for i in range(0, len(outputData)):
            connection.send(outputData[i].encode())
        
        connection.close()
        print('[thread] client', address, 'closing...')
        
    except IOError:
        connection.send('HTTP/1.1 404 Not found\r\n\r\n'.encode())
        connection.send('File not found'.encode())
        
        connection.close()
        print('[thread] client', address, 'closing...')

if __name__ == '__main__':
    webServer(6789)
