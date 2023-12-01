import pygame
import os

pygame.init()

#--colors--
white = (255,255,255)
grey = (100,100,100)
black = (0,0,0)


#--constants--
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
LOGO_WIDTH, LOGO_HEIGHT = 350, 200
BUTTON_WIDTH, BUTTON_HEIGHT = 300, 75
font = pygame.font.Font("freesansbold.ttf", 40)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  
pygame.display.set_caption("chess")

#--assets--
logo = pygame.image.load(os.path.join("chess assets", "Chess logo.png"))
logo = pygame.transform.scale(logo, (LOGO_WIDTH, LOGO_HEIGHT))   


def draw_buttons():
    play_button = pygame.draw.rect(screen, white, pygame.Rect(50, 350, BUTTON_WIDTH, BUTTON_HEIGHT))
    learn_button = pygame.draw.rect(screen, white, pygame.Rect(50, 450, BUTTON_WIDTH, BUTTON_HEIGHT))
    text_play = font.render("Play", True, black)
    text_learn = font.render("Learn", True, black)
    screen.blit(text_play, (157,370))
    screen.blit(text_learn, (145,470))
    return play_button, learn_button



def main():   
    running = True
    while running:
        screen.fill(grey)
        screen.blit(logo, (25, 75))  
        play_button, learn_button = draw_buttons() 
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if play_button.collidepoint(pos):
                    import pvp      #Play window is accessed from here
                    running = False

                if learn_button.collidepoint(pos):
                    pass     #Learn window is accessed from here


main()
