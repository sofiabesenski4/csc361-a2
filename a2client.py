#message to the server will have the format:
# ping sequence_number time


import time
#args: client's ip, client's socket, server IP, server socket
import sys
from socket import *
client_socket = socket(AF_INET, SOCK_DGRAM)



CLIENT_IP= sys.argv[1]
CLIENT_PORT = int(sys.argv[2])

client_socket.bind((CLIENT_IP,CLIENT_PORT))
client_socket.settimeout(1)
SERVER_IP = sys.argv[3]
SERVER_PORT = sys.argv[4]


print "Communicating with a server at adr {} and port {}".format(str(SERVER_IP),str(SERVER_PORT))	
i = 1
while (i<11):
	try:
		sending_time=time.time()
		message = "ping {} {}".format(i, sending_time) 
		client_socket.sendto(message, (SERVER_IP,SERVER_PORT))


		response, message = client_socket.recvfrom(1024)
		response_time = time.time() - sending_time
		print response, " RTT in milliseconds:", str(response_time*1000)
		
		
		i+=1;
	except:
		print "Request timed out"
