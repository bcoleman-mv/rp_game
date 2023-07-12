import socket
import pickle
from globals import HEADER

from player import Player

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Change to public ip address to play on the internet
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5050
        self.addr = (self.server, self.port)
        self.player = self.connect()
        
    def getPlayer(self) -> Player:
        return self.player
        
    def connect(self) -> Player:
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(HEADER))
        except:
            print("Could not connect...")
            pass
        
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(HEADER))
        except socket.error as e:
            print(e)