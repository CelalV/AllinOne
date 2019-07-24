import socket
import threading

class UDPServer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        print("UDP Server gestartet...\n")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('localhost', 1337))
        while True:
            data, adress = sock.recvfrom(1024)
            print(data.decode())
        return 0
