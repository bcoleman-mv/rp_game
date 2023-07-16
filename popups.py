import pygame
pygame.init()

from globals import *
from button import *

class Popup:
    def __init__(self, color:str, x_pos:int, y_pos:int, height:int, width:int, text:str, buttons:list):
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = height
        self.width = width
        self.text = text
        self.buttons = buttons
        
    def display_popup(self):
        self.background = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

        #draw background
        action = True
        pygame.draw.rect(WIN, "tan", self.background)

        #draw text
        self.font = pygame.font.Font("arial.ttf", 32)
        self.label = self.font.render(self.text, True, "black")
        self.labelRect = self.label.get_rect()
        self.labelRect.center = (self.width//2 + self.x_pos, self.y_pos+75)
        WIN.blit(self.label, self.labelRect)

        #draw buttons
        for i in range(len(self.buttons)):
            if Button.display_button(self.buttons[i]) == False:
                print("exit")
                action = False
            return action

class StartPopup(Popup):
    def __init__(self):
        startButton = Button("blue", 200, 200, 100, 50, "Start")        
        super().__init__(self.color, self.x_pos, self.y_pos, self.height, self.width, [startButton])
        self.background = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)


