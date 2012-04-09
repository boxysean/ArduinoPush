import socket
import sys
import time

HOST, PORT = "localhost", 8080
data = 0

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    # Connect to server and send data
#    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.sendall(str(data) + "\n")

    # Receive data from the server and shut down
    received = sock.recv(1024)
    print "Sent: {}".format(data)
    print "Received: {}".format(received)
    data = int(received)
    time.sleep(1)

#    sock.close()


