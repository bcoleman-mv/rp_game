from globals import *

class Circle:
    def __init__(self, color:str, size:int):
        self.color = color
        self.size = size
    
class Player(Circle):
    def __init__(self, color: str, size: int, position: pygame.Vector2 = None, direction:str = None):
        super().__init__(color, size)
        if position == None:
            self.position = pygame.Vector2(WIN.get_width() / 2, WIN.get_height() / 2)
        else:
            self.position = position
            
        if direction == None:
            self.direction = "right"
        else:
            self.direction = direction
        
    # def move(self, key:int):
    #     if key==pygame.K_w:
    #         self.position.y -= PLAYER_MOVE_DISTANCE
    #     if key==pygame.K_s:
    #         self.position.y += PLAYER_MOVE_DISTANCE
    #     if key==pygame.K_a:
    #         self.position.x -= PLAYER_MOVE_DISTANCE
    #     if key==pygame.K_d:
    #         self.position.x += PLAYER_MOVE_DISTANCE
    #     print(f"Player moved: {self.position.x}, {self.position.y}")
    
    def move_right(self):
        # self.change_direction("right")
        self.position.x += 1
        print("Moved right")
        
    def move_left(self):
        # self.change_direction("left")
        self.position.x -= 1
        print("Moved left")
        
    def move_up(self):
        # self.change_direction("up")
        self.position.y -= 1
        print("Moved up")
        
    def move_down(self):
        # self.change_direction("down")
        self.position.y += 1
        print("Moved down")
        
    def move(self):
        if self.direction == "left":
            self.move_left()
        elif self.direction == "right":
            self.move_right()
        elif self.direction == "up":
            self.move_up()
        elif self.direction == "down":
            self.move_down()
        print(f"Position: {self.position}")
            
    def change_direction(self, direction:str):
        if direction in ["left", "right", "up", "down"]:
            self.direction = direction
        else:
            raise ValueError(f"{self.direction} is not a valid direction")
            