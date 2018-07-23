#import socket module
import socket
#create socket object
s = socket.socket()

#connection to the server using connect()..
s.connect(('127.0.0.1', 4444))
#print data received ...
print s.recv(1024)

#close the connection
s.close
