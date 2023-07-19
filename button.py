import pygame
pygame.init()

from globals import *

class Button:
    def __init__(self, color:str, x_pos:int, y_pos:int, width:int, height:int, text:str):
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.text = text
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.font = pygame.font.Font("arial.ttf", 16)

    def display_button(self):
        action = True

        #get mouse position
        pos = pygame.mouse.get_pos()
        print(pos)
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            action = False

        pygame.draw.rect(WIN, self.color, self.rect)
        self.label = self.font.render(self.text, True, "black")
        self.label_rect = self.label.get_rect()
        self.label_rect.center = self.rect.center
        WIN.blit(self.label, self.label_rect)

        return action
        
        