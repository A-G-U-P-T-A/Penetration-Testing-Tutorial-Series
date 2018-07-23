#port_scanner in python
from threading import Thread # for speeding up scans
import socket 
#enter host details and range of ip address.....
host = raw_input('Enter host IP Address : ')
lb = int(raw_input('Enter lower range of port : '))
ub = int(raw_input('Enter upper range of port : '))
#list to store open ports
open_ports = []
threads = [] #list handling threads

def scanner(port):
	s = socket.socket()
	result = s.connect_ex((host, port))
	if result == 0:
		open_ports.append(port) #if connect returns 0 means port is open
		print((str(port))+ ' is open')
		s.close()

for i in range(lb, ub+1):
	t = Thread(target = scanner , args =  (i,))
	threads.append(t)
	t.start()
#at last print the list of open ports in the range mentioned..... 
print(open_ports)

#lets test it :)
