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
sequence_number = 122
client_socket.settimeout(1)


SERVER_IP = "127.0.0.1"
SERVER_PORT = 12000
sending_time = time.time()
message = "ping {} {}".format(sequence_number, sending_time) 
client_socket.sendto(message, (SERVER_IP,SERVER_PORT))


response, message = client_socket.recvfrom(1024)
response_time = time.time() - sending_time
print response, "in millisecond:", str(response_time*1000)
