import random
from uuid import UUID
import pygame
from pygame.colordict import THECOLORS
from globals import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from playerlist import PlayerList

MAX_CAPACITY = 3

class Game:
    def __init__(self):
        self.ready = False
        self.players = PlayerList(MAX_CAPACITY)
        
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
        player_color = self._get_random_color()
        player_position = pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        return Player(order, player_color, 20, player_position)
    
    def _get_random_color(self):
        r_color = random.choice(list(THECOLORS.keys()))
        not_avail_colors = [p.color for p in self.players.get_players()]
        if r_color not in not_avail_colors and r_color != "white":
            return r_color
        return self._get_random_color()
    
    def remove_player(self, playerId: UUID):
        rm_player = self.players.remove(playerId)
        self._update_player_order(rm_player.order)
        print(f"Player {rm_player.order} disconnected from the game")
        
    def _update_player_order(self, order):
        d = {k:self._subtract_order(v) if v.order > order else v for (k,v) in self.players.get_dict()}
        self.players = PlayerList(MAX_CAPACITY, d)

    @staticmethod
    def _subtract_order(player: Player):
        player.order -= 1
        return player
        
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