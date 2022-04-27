#!/usr/bin/python           # This is server.py file
	
import socket               # Import socket module
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1234                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
	
s.listen(5)                 # Now wait for client connection.
while True:
	clientsocket, address = s.accept()     # Establish connection with client.
	print(f"Connection from {address} has been established")
	clientsocket.send(bytes("Thank you for connecting", "utf-8"))
	#c.close()                # Close the connection
