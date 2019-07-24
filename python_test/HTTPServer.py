import socket
import threading

class HTTPServer(threading.Thread):

    
        
    def __init__(self):
        threading.Thread.__init__(self)
        self.TCP_IP = '127.0.0.1'
        self.TCP_PORT = 4444
        self.BUFFER_SIZE = 1024

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.TCP_IP, self.TCP_PORT))
        sock.listen(1)
        print("HTTP Server wurde gestartet...")
        
        while True:
            conn, addr = sock.accept()
            data = conn.recv(self.BUFFER_SIZE)
            print ("Daten: " + str(data))

httpserver = HTTPServer()
httpserver.start()
