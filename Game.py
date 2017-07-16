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

#init timer
start_timer = time()
struct = localtime(start_timer)                                                                                         #start timer


#game loop
stopGame = False
i = 0

while not stopGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stopGame = True
            pygame.quit()                                                                                               #quit game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            stopGame = True
        if event.type == pygame.MOUSEBUTTONUP and len(wl_array) > i:
            gameDisplay.fill(pygame.Color("black"))                                                                     #clean whole screen
            huidigWoord = font.render(wl_array[i], True, pygame.Color("green"))                                         #make new word
            gameDisplay.blit(huidigWoord, (400 - huidigWoord.get_width() // 2, 300 - huidigWoord.get_height() // 2))    #display new word
            i += 1                                                                                                      #increase i for array loop

    pygame.display.flip()
    clock.tick(60)
