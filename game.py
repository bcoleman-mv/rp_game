import random
from uuid import UUID
import uuid
import pygame
from globals import *
from player import Player
from playerlist import PlayerList

class Game:
    def __init__(self):
        self.id = uuid.uuid4()
        self.ready = False
        self.players = PlayerList(MAX_GAME_CAPACITY)
        
    def get_players(self):
        return self.players.get_players()
    
    def get_player(self, playerId: UUID):
        return self.players.get(playerId)
    
    def update_player(self, player: Player):
        self.players.update(player)
    
    def add_new_player(self):
        if self.max_capacity_reached():
            print("Could not add new player. Game has reached max capacity.")
            return None
        
        new_player = self._create_player()
        self.players.add(new_player)
        print(f"Player joined [{new_player.id}]")
        return new_player
    
    def _create_player(self):
        order = len(self.players) + 1
        player_color = self._get_available_color()
        player_position = pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        return Player(player_color, 20, order, player_position)
    
    def _get_available_color(self):
        r_color = random.choice(list(THECOLORS.keys()))
        not_avail_colors = [p.color for p in self.players.get_players()]
        if r_color not in not_avail_colors and r_color != "white":
            return r_color
        return self._get_available_color()
    
    def remove_player(self, playerId: UUID):
        rm_player = self.players.remove(playerId)
        print(f"Player {rm_player.order} disconnected from the game")
        self._update_player_order(rm_player.order)
        
    def _update_player_order(self, rm_order):
        for p in self.players.get_players():
            if p.order > rm_order:
                p.order -= 1
                self.players.update(p)
        
    def draw_players(self, WIN: pygame.surface):
        for player in self.players.get_players():
            player.draw(WIN)
        
    def no_players_remaining(self):
        return self.players.is_empty()
        
    def is_connected(self):
        return self.ready
    
    def max_capacity_reached(self):
        return self.players.is_full()
    
    def connect(self):
        self.ready = True
        print("New Game Started")
    
    def disconnect(self):
        self.ready = False