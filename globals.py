import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
KEYS = pygame.key.get_pressed()
WHITE = (255, 255, 255)
CLOCK = pygame.time.Clock()

PLAYER_MOVE_DISTANCE = 210