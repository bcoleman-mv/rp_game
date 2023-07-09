from globals import *

class Circle:
    def __init__(self, color:str, radius:float):
        self.color = color
        self.radius = radius
    
class Player(Circle):
    def __init__(self, color: str, size: int, position: pygame.Vector2 = None, direction:str = None):
        radius = size / 2
        super().__init__(color, radius)
        self.size = size
        
        if position == None:
            self.position = pygame.Vector2(WIN.get_width() / 2, WIN.get_height() / 2)
        else:
            self.position = position
            
        if direction == None:
            self.direction = "right"
        else:
            self.direction = direction
            
    
    def move_right(self):
        if self.position.x < WIDTH:
            self.change_direction("right")
            self.position.x += PLAYER_MOVE_DISTANCE
            print("Moved right")
        
    def move_left(self):
        if self.position.x > 0:
            self.change_direction("left")
            self.position.x -= PLAYER_MOVE_DISTANCE
            print("Moved left")
        
    def move_up(self):
        if self.position.y > 0:
            self.change_direction("up")
            self.position.y -= PLAYER_MOVE_DISTANCE
            print("Moved up")
        
    def move_down(self):
        if self.position.y < HEIGHT:
            self.change_direction("down")
            self.position.y += PLAYER_MOVE_DISTANCE
            print("Moved down")
            
    def change_direction(self, direction:str):
        if direction in ["left", "right", "up", "down"]:
            self.direction = direction
        else:
            raise ValueError(f"{self.direction} is not a valid direction")
            