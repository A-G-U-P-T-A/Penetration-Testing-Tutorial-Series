#http request example using scapy....
from scapy.all import *
#initialize packet sequence number src and dest. port numbers
seq = 12345
sport = 4444
dport = 80
#creating IP payload.....
ip_packet = IP(dst='www.google.com') #adding destination ip as www.google.com
#3 way tcp handshake for establishing connection
#creating a syn packet
syn_packet = TCP(sport=sport, dport=dport, flags='S', seq=seq)
packet = ip_packet/syn_packet
#sending packet and receiving syn+ack packet as response ....
synack_response = sr1(packet)
next_seq = seq + 1
#seding ack packet now.....
ack_packet = TCP(sport=sport, dport=dport, flags='A', seq=next_seq, ack=synack_response.seq+1)
send(ip_packet/ack_packet)
#now connection established lets do a http request :)
http_packet = TCP(sport=sport, dport=dport, flags='A', seq=next_seq, ack=synack_response.seq+1)
payload= "GET / HTTP/1.1\r\nHOST: www.google.com\r\n\r\n"
reply, error = sr(ip_packet/http_packet/payload, multi=1, timeout=1)
for r in reply:
	r[0].show2()
	r[1].show2()
#lets test it :)
