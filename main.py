from globals import *

from player import Player

# pygame setup
# pygame.init()

pygame.display.set_caption("Let's Roleplay!")

player_pos = pygame.Vector2(WIN.get_width() / 2, WIN.get_height() / 2)
player = Player("red", 30)


def draw_window(color: tuple[int,int,int]):
    WIN.fill(color)
    draw_player(player)
    pygame.display.update()

def draw_player(player: Player):
    pygame.draw.circle(WIN, player.color, player.position, player.radius)
    
def handle_movement(keys):
    if keys[pygame.K_w]: # up
        player.move_up()
    if keys[pygame.K_s]: # down
        player.move_down()
    if keys[pygame.K_a]: # left
        player.move_left()
    if keys[pygame.K_d]: # right
        player.move_right()

def main():
    running = True
    
    while running:
        CLOCK.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()
        handle_movement(keys)

        draw_window(WHITE)
        
    print("Game Ended")
    pygame.quit()
    

if __name__ == "__main__":
    main()