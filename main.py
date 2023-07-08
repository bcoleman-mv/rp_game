from globals import *

from player import Player

# pygame setup
# pygame.init()

pygame.display.set_caption("Let's Roleplay!")

player_pos = pygame.Vector2(WIN.get_width() / 2, WIN.get_height() / 2)
player1 = Player("red", 25)


def draw_window(color: tuple[int,int,int]):
    WIN.fill(color)
    pygame.display.update()

def draw_player(player: Player):
    pygame.draw.circle(WIN, player.color, player.position, player.size)
    pygame.display.update()

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_window(WHITE)
        draw_player(player1)
        
        if KEYS[pygame.K_w]:
            player1.move(pygame.K_w)
        if KEYS[pygame.K_s]:
            player1.move(pygame.K_s)
        if KEYS[pygame.K_a]:
            player1.move(pygame.K_a)
        if KEYS[pygame.K_d]:
            player1.move(pygame.K_d)

        pygame.display.flip()
        # dt = CLOCK.tick(60) / 1000
        
    print("Game Ended")
    pygame.quit()
    

if __name__ == "__main__":
    main()