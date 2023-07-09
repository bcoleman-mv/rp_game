from globals import *
import pygame
from player import Player
from network import Network

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WIN.fill(COLOR_WHITE)
pygame.display.set_caption("Let's Roleplay!")

leftPos = pygame.Vector2(SCREEN_WIDTH * 0.33, SCREEN_HEIGHT * 0.5)
rightPos = pygame.Vector2(SCREEN_WIDTH * 0.67, SCREEN_HEIGHT * 0.5)

# p1 = Player("blue", 15, leftPos)
# p2 = Player("red", 15, rightPos)

def redraw_window(color: tuple[int,int,int], player1: Player, player2: Player):
    WIN.fill(color)
    player1.draw(WIN)
    player2.draw(WIN)
    pygame.display.update()

def main():
    running = True
    n = Network()
    p1 = n.getP()
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        p2 = n.send(p1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Game Ended")
                pygame.quit()
            
        p1.move()
        redraw_window(COLOR_WHITE, p1, p2)
    

if __name__ == "__main__":
    main()