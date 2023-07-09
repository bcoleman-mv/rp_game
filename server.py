from globals import *
import pygame
import socket
from _thread import *
import sys

server = "10.0.0.9"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, Server Started")

def read_pos(str: str):
    print("str (server): ", str)
    str = str.split(",")
    x = int(float(str[0]))
    y = int(float(str[1]))
    return pygame.Vector2(x, y)

def make_pos(pos: pygame.Vector2):
    return str(pos.x) + "," + str(pos.y)

leftPos = pygame.Vector2(int(SCREEN_WIDTH * 0.33), int(SCREEN_HEIGHT * 0.5))
rightPos = pygame.Vector2(int(SCREEN_WIDTH * 0.67), int(SCREEN_HEIGHT * 0.5))

pos = [leftPos, rightPos]

def threaded_client(conn, player: int):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data
            
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                    
                print("Received: ", data)
                print("Sending:  ", reply)
                
            conn.sendall(str.encode(make_pos(reply)))
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