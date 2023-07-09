import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
KEYS = pygame.key.get_pressed()
WHITE = (255, 255, 255)
CLOCK = pygame.time.Clock()
DT = 0

PLAYER_MOVE_DISTANCE = 5

clientNumber = 0