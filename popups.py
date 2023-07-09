from globals import *

pygame.init()

class Popup:
    def __init__(self, color:str, x_pos:int, y_pos:int, height:int, width:int, text:str, num_buttons:int):
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = height
        self.width = width
        self.text = text
        self.num_buttons = num_buttons
        self.background = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def display_popup(self):
        #draw background
        pygame.draw.rect(WIN, "tan", self.background)

        #draw text
        self.font = pygame.font.Font("arial.ttf", 32)
        self.label = self.font.render(self.text, True, "black")
        self.labelRect = self.label.get_rect()
        self.labelRect.center = (self.width//2 + self.x_pos, self.y_pos+75)
        WIN.blit(self.label, self.labelRect)

        #draw buttons
        self.button_width = ((1/self.num_buttons)*self.width) - ((2/10*self.width))
        self.button_height = self.width/8
        self.button_space = (self.width - (self.num_buttons * self.button_width))/(self.num_buttons + 2)

        for i in range(self.num_buttons):
            button_y_pos = (self.button_height * 3) + self.height
            button_x_pos = (((i+1)*self.button_space) + (i*self.button_width))+self.x_pos
            button_rect = pygame.Rect(button_x_pos, button_y_pos, self.button_width, self.button_height)
            pygame.draw.rect(WIN,"pink",button_rect)
        