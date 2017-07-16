#import
import pygame
import random
import time

#init
pygame.init()

#init display
gameDisplay = pygame.display.set_mode((800, 600))
gameDisplay.fill((255, 255, 255))
pygame.display.set_caption('-- KIH --')

#init text
font = pygame.font.SysFont("comicsansms", 50)
huidigWoord = font.render("Press mouse button to start", True, (0, 0, 0))
gameDisplay.blit(huidigWoord, (400 - huidigWoord.get_width() // 2, 300 - huidigWoord.get_height() // 2))
font = pygame.font.SysFont("comicsansms", 75)                                                                           #incrase font size

#clock
clock = pygame.time.Clock()

#lees array uit txt file
with open('wl.txt') as wl:
    wl_array = wl.readlines()
    
#remove \n from wl_array
wl_array = [x.strip() for x in wl_array]

#shuuffle array
random.shuffle(wl_array)

#game loop
stopGame = False
dead = False
i = 0

while not stopGame:
    #if first time
    if i == 0:
        #start timer
        timeout = time.time() + 10 #10 sec
        
    #if last word
    if len(wl_array) <= i:
        gameDisplay.fill(pygame.Color("black"))                                                                     #clean whole screen
        huidigWoord = font.render(">> ?huh? <<", True, pygame.Color("red"))                                         #make new word
        gameDisplay.blit(huidigWoord, (400 - huidigWoord.get_width() // 2, 300 - huidigWoord.get_height() // 2))    #display new word
        dead = True

    #time == up
    if time.time() > timeout:
        gameDisplay.fill(pygame.Color("black"))                                                                     #clean whole screen
        huidigWoord = font.render("GAME OVER", True, pygame.Color("red"))                                           #make new word
        gameDisplay.blit(huidigWoord, (400 - huidigWoord.get_width() // 2, 300 - huidigWoord.get_height() // 2))    #display new word
        dead = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
            pygame.quit()                                                                                           #quit game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            dead = True
        if event.type == pygame.MOUSEBUTTONUP and len(wl_array) > i:
            gameDisplay.fill(pygame.Color("black"))                                                                 #clean whole screen
            huidigWoord = font.render(wl_array[i], True, pygame.Color("green"))                                     #make new word
            gameDisplay.blit(huidigWoord, (400 - huidigWoord.get_width() // 2, 300 - huidigWoord.get_height() // 2))#display new word
            i += 1                                                                                                  #increase i for array loop

    #dead
    if dead:
        mouse = pygame.mouse.get_pos()
        #if mouse is over button
        if 150+300 > mouse[0] > 150 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, pygame.Color("green"), (300, 400, 300, 50))
        else:
            pygame.draw.rect(gameDisplay, pygame.Color("orange"), (300, 400, 300, 50))

        #startOver text                                                                     
        huidigWoord = font.render("-- Opnieuw --", True, pygame.Color("yellow"))                                           #make new word
        gameDisplay.blit(huidigWoord, (300, 400, 300, 50))    #display new word

            
    time.sleep(.1)
    pygame.display.flip()
    clock.tick(60)
