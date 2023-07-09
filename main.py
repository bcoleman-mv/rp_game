from globals import *
import pygame
from player import Player
from network import Network

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WIN.fill(COLOR_WHITE)
pygame.display.set_caption("Let's Roleplay!")

def read_pos(str: str):
    print("str (client): ", str)
    str = str.split(",")
    x = int(float(str[0]))
    y = int(float(str[1]))
    return pygame.Vector2(x, y)

def make_pos(pos: pygame.Vector2):
    return str(pos.x) + "," + str(pos.y)

def redraw_window(color: tuple[int,int,int], player1: Player, player2: Player):
    WIN.fill(color)
    player1.draw(WIN)
    player2.draw(WIN)
    pygame.display.update()

def main():
    running = True
    clock = pygame.time.Clock()
    
    n = Network()
    recv_network_pos = n.getPos()
    p1_startPos = read_pos(recv_network_pos)
    player1 = Player("red", 30, p1_startPos)
    
    p2_startPos = pygame.Vector2(WIN.get_width() / 2, WIN.get_height() / 2)
    player2 = Player("blue", 30, p2_startPos)

    while running:
        clock.tick(60)
        
        strPos = make_pos(player1.get_position())
        decoded_pos = n.send(strPos)
        
        if not decoded_pos == '':
            p2Pos = read_pos(decoded_pos)
        else:
            p2Pos = p2_startPos
        
        player2.update_position(p2Pos)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Game Ended")
                pygame.quit()
            
        player1.move()
        redraw_window(COLOR_WHITE, player1, player2)
    

if __name__ == "__main__":
    main()