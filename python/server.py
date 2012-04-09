import SocketServer
import time

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
#        self.data = self.request.recv(1024).strip()
#        print "{} wrote: {}".format(self.client_address[0], self.data)
#        self.request.sendall(str(int(self.data)+1))
	print "handling connection!"
	while True:
		self.request.sendall("L")
		print "LOW"
		time.sleep(1)
		self.request.sendall("H")
		print "HIGH"
		time.sleep(1)

    def handle_timeout(self):
        print "CONNECTION TIMED OUT"

if __name__ == "__main__":
    HOST, PORT = "192.168.1.150", 8082
#    HOST, PORT = "0.0.0.0", 8082

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.timeout = 10

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

