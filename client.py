import sys
from game import Game
from globals import *
import pygame
from player import Player
from network import Network


WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WIN.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Let's Roleplay!")

def redraw_window(game: Game):
    WIN.fill(BACKGROUND_COLOR)
    game.draw_players(WIN)
    
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
        pygame.display.update()

if __name__ == "__main__":
    main()