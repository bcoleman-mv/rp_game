import sys
from game import Game
from globals import *
import pygame
from player import Player
from network import Network


WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WIN.fill(COLOR_WHITE)
pygame.display.set_caption("Let's Roleplay!")

def redraw_window(game: Game):
    WIN.fill(COLOR_WHITE)
    game.draw_players(WIN)
    pygame.display.update()
    
def main():
    running = True
    clock = pygame.time.Clock()
    n = Network()
    player = n.getPlayer()
    print("You are player", player.order)
    
    while running:
        clock.tick(FPS)
        try:
            game: Game = n.send(player)
        except:
            running = False
            print("Could not get game")
            break
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        
        player.move()
        redraw_window(game)

main()