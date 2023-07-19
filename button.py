import pygame
pygame.init()

from globals import *

class Button:
    def __init__(self, x_pos:int, y_pos:int, width:int, height:int, text:str):
        self.image = pygame.transform.scale(pygame.image.load('buttons.png').convert_alpha(), (width, height))
        self.text = text
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.font = pygame.font.Font("prstart.ttf", 10)

    def display_button(self):
        action = True

        #get mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            action = False

        WIN.blit(self.image, (self.rect.x, self.rect.y))
        self.label = self.font.render(self.text, True, "white")
        self.label_rect = self.label.get_rect()
        self.label_rect.center = self.rect.center
        WIN.blit(self.label, self.label_rect)

        return action
        
        