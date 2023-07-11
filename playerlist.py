from uuid import UUID
from player import Player


class PlayerList:
    def __init__(self, max_capacity: int, players: dict[UUID, Player] = None):
        self.MAX = max_capacity
        self.player_dict = players if players else {}
        
    def __len__(self):
        return len(self.player_dict)
    
    def get_players(self):
        return list(self.player_dict.values())
    
    def get_ids(self):
        return list(self.player_dict.keys())
    
    def get_dict(self):
        return self.player_dict.items()
    
    def get(self, playerId: UUID):
        return self.player_dict[playerId]
    
    def update(self, player: Player):
        self.player_dict[player.id] = player
    
    def add(self, player: Player):
        if self.is_full():
            return None
        self.player_dict[player.id] = player
        return player
    
    def remove(self, playerId: UUID):
        return self.player_dict.pop(playerId)
        
    def is_empty(self):
        return len(self.player_dict) == 0
    
    def is_full(self):
        return len(self.player_dict) == self.MAX
