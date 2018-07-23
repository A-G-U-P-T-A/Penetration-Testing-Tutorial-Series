#import socket library
import socket
#creating a socket object using socket() function.
s = socket.socket()
#creating a port on which the server will listen at.
p = 4444
#calling bind() function to bind ip address with port number (important step)
s.bind(('', p))
#starting the socket listener mode...
s.listen(5)
#the 5 mentioned here means the server can accept max 5 connections.
while True:
	c, addr = s.accept() #accepting incoming connection
	c.send('Connected to server !!!') #sending data to a connected client.
	c.close() #closes the connection with the client.
#lets check whether its working or not....
