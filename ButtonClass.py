import pygame



class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        
        action = False

        #Get mouse cursor position
        pos = pygame.mouse.get_pos()


        #Check if mouse over button and clicked conditions
        if self.rect.collidepoint(pos): #get_pressed = 1 means clicked = 0 means not clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #[0] = left mouse click [1] = scroll wheel clock [2] = right click
                self.clicked = True 
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return 