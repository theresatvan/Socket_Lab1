# Socket_Lab1
Socket programming lab #1 for NYU Tandon CS-GY 6843

## To execute *server.py*
```
python server.py
```

*server.py* runs on port 6789 and will listen for exactly one TCP connection. The program will then extract the filename from the message request, extracting the second word from the message. (e.g, a message request `GET /somefile.html ...` the program will extract `/somefile.html` and search its server directory for this file)

### If requested file found
The server socket will send a `HTTP 200 OK` response header line to the client socket, and then send the contents of the requested file to the client socket in multiple chunks.

### If requested file is not found
The server socket will send a `HTTP 404 Not Found` response header line to the client socket as well as a `File not found` message.

## To execute *multiserver.py*
```
python multiserver.py
```

*multiserver.py* runs on port 6789 and will listen for up to five TCP connections. For each TCP connection, the program will create a new thread and formulate a response there. The program will then extract the filename from the message request, extracting the second word from the message. (e.g, a message request `GET /somefile.html ...` the program will extract `/somefile.html` and search its server directory for this file)

### If requested file found
The server socket will send a `HTTP 200 OK` response header line to the client socket, and then send the contents of the requested file to the client socket in multiple chunks.

### If requested file does not found
The server socket will send a `HTTP 404 Not Found` response header line to the client socket as well as a `File not found` message.

## If attempting to send a request to either *server.py* or *multiserver.py* via browser
```
http://<server IP address>:6789/<filename>
```
## To execute *client.py*
```
python client.py <server IP address> 6789 <filename>
```
