from dataclasses import dataclass
from enum import Enum
import uuid
from globals import *
import pygame

class Circle:
    def __init__(self, color: str = "black", radius: float = 20):
        self.color = color
        self.radius = radius
        
    def _draw(self, WIN: pygame.Surface, position: pygame.Vector2):
        pygame.draw.circle(WIN, self.color, position, self.radius)
        

class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"
    
PLAYER_MOVE_DISTANCE = 5

CENTERSCREEN = pygame.Vector2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

class Player(Circle):
    def __init__(self, color: str = None, size: int = 20, order: int = -1,
        position: pygame.Vector2 = CENTERSCREEN, direction: Direction = Direction.UP):
        radius = size / 2
        super().__init__(color, radius)
        self.id = uuid.uuid4()
        self.order = order
        self.size = size
        self.position = position
        self.direction = direction

    def get_position(self):
        return self.position
        
    def draw(self, WIN: pygame.Surface):
        self._draw(WIN, self.position)
    
    def move_left(self):
        if self.position.x > (0 + self.radius):
            self.direction = Direction.LEFT
            self.position.x -= PLAYER_MOVE_DISTANCE
            
    def move_right(self):
        if self.position.x < (SCREEN_WIDTH - self.radius):
            self.direction = Direction.RIGHT
            self.position.x += PLAYER_MOVE_DISTANCE
        
    def move_up(self):
        if self.position.y > (0 + self.radius):
            self.direction = Direction.UP
            self.position.y -= PLAYER_MOVE_DISTANCE
        
    def move_down(self):
        if self.position.y < (SCREEN_HEIGHT - self.radius):
            self.direction = Direction.DOWN
            self.position.y += PLAYER_MOVE_DISTANCE
            
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