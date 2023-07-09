import pickle
from globals import *
import pygame
import socket
from _thread import *
import sys

from player import Player

server = "10.0.0.9"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, Server Started")

leftPos = pygame.Vector2(SCREEN_WIDTH * 0.33, SCREEN_HEIGHT * 0.5)
rightPos = pygame.Vector2(SCREEN_WIDTH * 0.67, SCREEN_HEIGHT * 0.5)

players = [Player("blue", 15, leftPos), Player("red", 15, rightPos)]

def threaded_client(conn, player: int):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                    
                print("Received: ", data)
                print("Sending:  ", reply)
                
            conn.sendall(pickle.dumps(reply))
        except:
            break
    
    
    print("Lost Connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1