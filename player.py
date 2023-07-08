from globals import *

class Circle:
    def __init__(self, color:str, size:int):
        self.color = color
        self.size = size

class Player(Circle):
    def __init__(self, color: str, size: int, position: pygame.Vector2 = None):
        super().__init__(color, size)
        if position == None:
            self.position = pygame.Vector2(WIN.get_width() / 2, WIN.get_height() / 2)
        else:
            self.position = position
        
    def move(self, key:int):
        if key==pygame.K_w:
            self.position.y -= PLAYER_MOVE_DISTANCE
        if key==pygame.K_s:
            self.position.y += PLAYER_MOVE_DISTANCE
        if key==pygame.K_a:
            self.position.x -= PLAYER_MOVE_DISTANCE
        if key==pygame.K_d:
            self.position.x += PLAYER_MOVE_DISTANCE