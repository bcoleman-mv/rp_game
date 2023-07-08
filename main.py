from globals import *

from player import Player

# pygame setup
# pygame.init()

pygame.display.set_caption("Let's Roleplay!")

player_pos = pygame.Vector2(WIN.get_width() / 2, WIN.get_height() / 2)
player1 = Player("red", 25)


def draw_window(color: tuple[int,int,int], player: Player):
    WIN.fill(color)
    draw_player(player)
    pygame.display.update()

def draw_player(player: Player):
    pygame.draw.circle(WIN, player.color, player.position, player.size)

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if player1.position.x >= WIDTH:
            player1.change_direction("left")
        elif player1.position.x <= 0:
            player1.change_direction("right")
        elif player1.position.y >= HEIGHT:
            player1.change_direction("up")
        elif player1.position.y <= 0:
            player1.change_direction("down")
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.change_direction("up")
        if keys[pygame.K_s]:
            player1.change_direction("down")
        if keys[pygame.K_a]:
            player1.change_direction("left")
        if keys[pygame.K_d]:
            player1.change_direction("right")
        
        player1.move()
        draw_window(WHITE, player1)
        
        # if KEYS[pygame.K_w]:
        #     player1.move(pygame.K_w)
        # if KEYS[pygame.K_s]:
        #     player1.move(pygame.K_s)
        # if KEYS[pygame.K_a]:
        #     player1.move(pygame.K_a)
        # if KEYS[pygame.K_d]:
        #     player1.move(pygame.K_d)

        # pygame.display.flip()
        # dt = CLOCK.tick(60) / 1000
        
    print("Game Ended")
    pygame.quit()
    

if __name__ == "__main__":
    main()