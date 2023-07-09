from globals import *

pygame.init()

class Popup:
    def __init__(self, color:str, x_pos:int, y_pos:int, height:int, width:int, text:str, button_text:list):
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = height
        self.width = width
        self.text = text
        self.button_text = button_text
        self.buttin_font = pygame.font.Font("arial.ttf", 16)
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
        print(len(self.button_text))
        self.button_width = ((1/len(self.button_text))*self.width) - ((2/10*self.width))
        self.button_height = self.width/8
        self.button_space = (self.width - (len(self.button_text) * self.button_width))/(len(self.button_text) + 1)

        for i in range(len(self.button_text)):
            button_y_pos = (self.button_height * 3) + self.height/2
            button_x_pos = (((i+1)*self.button_space) + (i*self.button_width))+self.x_pos
            button_rect = pygame.Rect(button_x_pos, button_y_pos, self.button_width, self.button_height)
            pygame.draw.rect(WIN,"pink",button_rect)

            button_label = self.buttin_font.render(self.button_text[i], True, "black")
            WIN.blit(button_label, button_rect)
        