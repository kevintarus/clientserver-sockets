#!/usr/bin/python           # This is client.py file
	
import socket               # Import socket module
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1234                # Reserve a port for your service.
	
s.connect((host, port))
msg = s.recv(1024)
print(msg.decode("utf-8"))
#s.close()                     # Close the socket when done
