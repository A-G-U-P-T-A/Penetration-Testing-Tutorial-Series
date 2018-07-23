#ns look up script in python
import socket
#get the corresponding ip address
print(socket.gethostbyname("www.google.com"))
#get the corresponding domain name
print(socket.gethostbyaddr("8.8.8.8"))
