import pygame
import ButtonClass



pygame.init()

WIDTH = 800
HEIGHT = 600

Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Menu")

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#game variables
game_paused = False

#define colors
TEXT_COL = (255, 255, 255)

def resize_image(image):
    return pygame.transform.scale(image, (200, 200))
#load images
resume_icon = pygame.image.load("resume-icon.png").convert_alpha()
resume_icon = resize_image(resume_icon)
exit_icon = pygame.image.load("Button-Close-icon.png").convert_alpha()
exit_icon = resize_image(exit_icon)
option_icon = pygame.image.load("option-icon.png").convert_alpha()
option_icon = resize_image(option_icon)


#Create Button instances
resume_button = ButtonClass.Button(50, 200, resume_icon, 1)
exit_button = ButtonClass.Button(300, 200, exit_icon, 1)
option_button = ButtonClass.Button(525, 200, option_icon, 1)





def draw_text(text, font, text_col, x, y):

    img = font.render(text, True, text_col)
    Screen.blit(img, (x, y))



run = True

while run:

    
    
    #check if game paused
    if game_paused:
        Screen.fill((250, 198, 53))
        resume_button.draw(Screen)
        exit_button.draw(Screen)
        option_button.draw(Screen)
    else:
        Screen.fill((0, 191, 255))
        draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
