import pygame
import sys

class Screen:
    def __init__(self, surface):
        #Instance variables of each screen
        self.surface = surface
        self.background_colour = (192, 192, 192)
        self.button_colour = (131, 139, 139)
        self.black = (0, 0, 0)

    #Draws text onto the screen
    def create_text(self, font_size, text, position, font_style = "Comic Sans MS"):
        myfont = pygame.font.SysFont(font_style, font_size)
        textsurface = myfont.render(text, False, self.black)
        self.surface.blit(textsurface, position)

    #Creates button on the screen
    def create_button(self, x, y, width, height, font_size, button_colour, text, position):
        pygame.draw.rect(self.surface, button_colour, (x, y, width, height))
        pygame.draw.line(self.surface, self.black, (x, y), (x, y + height), 5)
        pygame.draw.line(self.surface, self.black, (x + width, y), (x + width, y + height), 5)
        pygame.draw.line(self.surface, self.black, (x, y), (x + width, y), 5)
        pygame.draw.line(self.surface, self.black, (x, y + height), (x + width, y + height), 5)
        self.create_text(font_size, text, position)

    #Changes the colour of the button when the mouse is on the button
    def change_button_colour(self, x, y, width, height, font_size, text, position):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.Rect(x, y, width, height).collidepoint(mouse_pos):
            self.create_button(x, y, width, height, font_size, (255, 100, 100), text, position)

    #Initializes button with all capabilities
    def initialize_button(self, x, y, width, height, font_size, button_colour, text, position):
        self.create_button(x, y, width, height, font_size, button_colour, text, position)
        self.change_button_colour(x, y, width, height, font_size, text, position)

    #Checks if button has been pressed
    def button_pressed(self, x, y, width, height):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and pygame.Rect(x, y, width, height).collidepoint(mouse_pos):
            return True
    
    #Create GUI for Language Classifier
    def create_language_gui(self, text, predicted_language):
        self.surface.fill((238, 213, 183))
        self.create_text(70, "Language Classifier", (240, 5))
        pygame.draw.rect(self.surface, (255, 255, 255), (150, 130, 800, 250))
        self.initialize_button(150, 450, 300, 100, 60, (193, 205, 205), "Reset", (215, 455))
        self.initialize_button(650, 450, 300, 100, 60, (193, 205, 205), "Classify", (690, 455))
        self.create_text(40, str(len(text)) + "/120", (800, 380))
        self.create_text(50, "Predicted Language: " + str(predicted_language), (170, 570))




