import pygame
pygame.init()

from globals import *
from button import *

class Popup:
    def __init__(self, x_pos:int, y_pos:int, height:int, width:int, text:str, buttons:list):
        self.image = pygame.transform.scale(pygame.image.load('popup.png').convert_alpha(), (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.text = text
        self.buttons = buttons
        self.rect = POPUP_IMG.get_rect()
        
        
    def display_popup(self):
        self.rect.center = WIN.get_rect().center
        WIN.blit(self.image, (self.rect.centerx- (self.image.get_width()/2), self.rect.centery - (self.image.get_height()/2)))
        action = True

        #draw text
        self.font = pygame.font.Font("arial.ttf", 32)
        self.label = self.font.render(self.text, True, "black")
        self.labelRect = self.label.get_rect()
        self.labelRect.center = self.rect.centerx, self.rect.centery - self.rect.height/2
        WIN.blit(self.label, self.labelRect)

        #draw buttons
        for i in range(len(self.buttons)):
             if Button.display_button(self.buttons[i]) == False:
                 print("exit")
                 action = False
             return action

class StartPopup(Popup):
    action = True
    def __init__(self):
        startButton = Button("blue", 200, 200, 100, 50, "Start")        
        super().__init__(self.color, self.x_pos, self.y_pos, self.height, self.width, [startButton])
        self.background = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

        if Button.display_button(startButton) == False:
            action = False


