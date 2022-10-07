# import socket module
from socket import *
import sys  # In order to terminate the program and receive arguments
import time # In order to set timeout function

def webClient(args=sys.argv[0:]):
    try:
        name, port, filename = args[1], int(args[2]), args[3]
        clientSocket = socket(AF_INET,SOCK_STREAM)  # Create TCP socket
        clientSocket.connect((name, port))
        
        data = 'GET /' + filename
        clientSocket.send(data.encode())    # send filename to server socket
        
        print('From Server:')
        recvAll(clientSocket)
        
        clientSocket.close()
        
    except IndexError:
        print('Input error.')
        
    except ConnectionRefusedError:
        print('Connection refused.')
        
    sys.exit()  # Terminate program

# ensures client receives and prints whole reponse from server
def recvAll(clientSocket,timeout=1):
    begin = time.time()
    while True:
        if time.time() - begin > timeout:
            break
        
        response = clientSocket.recv(1024)
        if response:
            print(response.decode())
            begin = time.time()
        else:
            time.sleep(1)

if __name__ == '__main__':
    webClient(args=sys.argv[0:])