from calendar import c
from curses.ascii import ESC
import pygame
from pygame.locals import * 
from pygame import mixer
import time, datetime 

pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((800,600))

#declare colours, images, sounds, fonts
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)
Calibri60 = pygame.font.SysFont("Calibri", 60)



#variables for keeping track of my game players etc.timer

quit = False

mouse_x = 0
mouse_y = 0
click = False
cps = 0
counter = 0
#main game loop
while  not quit:



    #process events
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            quit = True 
        elif event.type == MOUSEBUTTONDOWN:       
                click = True
                if click == True:
                    spacebar_sfx = mixer.Sound("spacebar_soundfx.mp3")
                    spacebar_sfx.play()
                    counter = counter + 1
        elif event.type == MOUSEBUTTONUP:
            click = False
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
          
    

    #perform calculations
    


    #draw graphics
    window.fill(white)
    label = Calibri60.render("Hello Pygame!", 1, black,)
    window.blit(label, (258,100))
    timer_text = Calibri60.render("Timer:" + str(counter),1,red )
    if click:
        space_pressed = Calibri60.render("Click",1, green)
    else:
        space_pressed = Calibri60.render("Click",1, red)
    window.blit(space_pressed, (100,500))
    click_no = Calibri60.render("Clicks:" + str(counter), 1, red)
    window.blit(click_no, (300,400))

    pygame.display.update()
    fps.tick(25)

#loop over, game over
pygame.quit()


