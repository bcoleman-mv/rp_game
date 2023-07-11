import pickle
import threading
from uuid import UUID
from game import Game
from globals import *
import socket
from player import Player

PORT = 5050
# Change to public ip address to run on internet
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind(ADDR)
except socket.error as e:
    str(e)

def handle_client(conn, addr, playerId: UUID, game: Game):
    player = game.get_player(playerId)
    conn.send(pickle.dumps(player))
    
    while True:
        try:
            player_data = pickle.loads(conn.recv(2048))
            
            if game.is_connected():
                
                if not player_data:
                    break
                
                game.update_player(player_data)
                conn.sendall(pickle.dumps(game))
            else:
                break
            
        except:
            break
    
    game.remove_player(playerId)
    conn.sendall(pickle.dumps(game))

    if game.no_players_remaining():
        game.disconnect()
    
    conn.close()

game = Game()

def start():
    print("\n[STARTING] Server is starting...")
    
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}\n")
    
    while True:
        conn, addr = server.accept()
        
        if not game.is_connected():
            game.connect()
            
        if not game.max_capacity_reached():
            print(f"\n[NEW CONNECTION] {addr} connected.")
            player = game.add_new_player()
            thread = threading.Thread(
                target=handle_client, args=(conn, addr, player.id, game))
            thread.start()
            print(f"\n[ACTIVE CONNECTIONS] {threading.active_count() - 1}\n")

start()