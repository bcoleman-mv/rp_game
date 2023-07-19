import pygame

pygame.init()


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
KEYS = pygame.key.get_pressed()
WHITE = (255, 255, 255)
CLOCK = pygame.time.Clock()
DT = 0
PLAYER_MOVE_DISTANCE = 5
START_POPUP_HEIGHT = 150
START_POPUP_WIDTH = 300
START_POPUP_X = WIDTH/2
START_POPUP_Y = HEIGHT/2

clientNumber = 0