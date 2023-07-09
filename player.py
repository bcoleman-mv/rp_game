from globals import *
import pygame

class Circle:
    def __init__(self, color:str, radius:float):
        self.color = color
        self.radius = radius
        
    def _draw_shape(self, WIN: pygame.Surface, position: pygame.Vector2):
        pygame.draw.circle(WIN, self.color, position, self.radius)

    
class Player(Circle):
    def __init__(self, color: str, size: int, position: pygame.Vector2, direction:str = None):
        radius = size / 2
        super().__init__(color, radius)
        self.size = size
        
        if position == None:
            self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            # self.x = position.x
            # self.y = position.y
        else:
            self.position = position
            # self.x = position.x
            # self.y = position.y
            
        if direction == None:
            self.direction = "right"
        else:
            self.direction = direction
            
    def get_position(self):
        return self.position
    
    def update_position(self, pos: pygame.Vector2):
        self.position = pos
        
    def draw(self, WIN: pygame.Surface):
        self._draw_shape(WIN, self.position)
    
    def move_right(self):
        if self.position.x < SCREEN_WIDTH:
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
        if self.position.y < SCREEN_HEIGHT:
            self.change_direction("down")
            self.position.y += PLAYER_MOVE_DISTANCE
            print("Moved down")
            
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: # up
            self.move_up()
        if keys[pygame.K_s]: # down
            self.move_down()
        if keys[pygame.K_a]: # left
            self.move_left()
        if keys[pygame.K_d]: # right
            self.move_right()
        
            
    def change_direction(self, direction:str):
        if direction in ["left", "right", "up", "down"]:
            self.direction = direction
        else:
            raise ValueError(f"{self.direction} is not a valid direction")
            