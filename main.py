import pygame
import os

pygame.init()

#--colors--
white = (255,255,255)
grey = (100,100,100)
grey_light = (150,150,150)
black = (0,0,0)

#--constants--
screen_width, screen_height = 400, 600
logo_width, logo_height = 350, 200
button_width, button_height = 250, 75
montserrat = "fonts/Montserrat/Montserrat-ExtraBold.ttf"
font = pygame.font.Font(montserrat, 37)

screen = pygame.display.set_mode([screen_width, screen_height])  
pygame.display.set_caption("chess")

#--assets--
logo = pygame.image.load(os.path.join("chess assets", "Chess logo.png"))
logo = pygame.transform.scale(logo, (logo_width, logo_height))   


def draw_buttons():
    play_button = pygame.draw.rect(screen, white, pygame.Rect(75, 350, button_width, button_height), 0, 10)
    learn_button = pygame.draw.rect(screen, white, pygame.Rect(75, 450, button_width, button_height), 0, 10)
    text_play = font.render("Play", True, black)
    text_learn = font.render("Learn", True, black)
    screen.blit(text_play, (157,365))
    screen.blit(text_learn, (145,465))
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
