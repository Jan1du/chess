import pygame
import os
import time
import pvp
from pvp import (
    colors,
    width,
    height
)

pygame.init()


#--Constants--#
img_width = img_height = 425
button_width, button_height = 250, 75


#--Variables--#
play_time = 0

#--assets--#
montserrat = "fonts/Montserrat/Montserrat-Bold.ttf"
font = pygame.font.Font(montserrat, 37)
arc = pygame.image.load(os.path.join("chess assets", "arc.png"))
arc = pygame.transform.scale(arc, (180, 200))
image = pygame.image.load(os.path.join("chess assets", "chess_image.png"))
image = pygame.transform.scale(image, (img_width, img_height))

screen = pygame.display.set_mode([width, height])  
pygame.display.set_caption("chess")

def display_time():
  mins_played = font.render(str(play_time), True, colors.white)
  mins = font.render("mins", True, colors.white)
  screen.blit(mins_played, (145,150))
  screen.blit(mins, (145, 185))

def draw_buttons():
    play_button = pygame.draw.rect(screen, colors.blue, pygame.Rect(75, 350, button_width, button_height), 0, 10)
    learn_button = pygame.draw.rect(screen, colors.blue, pygame.Rect(75, 450, button_width, button_height), 0, 10)
    text_play = font.render("PLAY", True, colors.white)
    text_learn = font.render("LEARN", True, colors.white)
    screen.blit(text_play, (148,365))
    screen.blit(text_learn, (137,465))
    return play_button, learn_button



def main():   
    running = True
    #startTime = time.time()
    while running:
        #gametime = time.time() - startTime
        #play_time = round(gametime/60, 3)

        screen.fill(colors.grey)
        play_button, learn_button = draw_buttons() 
        screen.blit(arc, (90,90))
        screen.blit(image, (415,95))
        display_time()
        pygame.display.flip()

        #changes the cursor when the cursor is within the button
        mouse_pos = pygame.mouse.get_pos()
        if 75 <= mouse_pos[0] <= 325 and 350 <= mouse_pos[1] <= 425:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)        
        
        elif 75 <= mouse_pos[0]<= 325 and 450 <= mouse_pos[1] <= 525:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False          

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if play_button.collidepoint(pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) #Changes the cursor back to normal
                    pvp.main()  #Play window is accessed from here
                    running = False

                if learn_button.collidepoint(pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) #Changes the cursor back to normal
                    pass     #Learn window is accessed from here

main()
