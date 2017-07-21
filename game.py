# Screen Res 800x480 original screensize
# We use 720x480

# Import
import pygame
import random
import time

# Constants
TIMELIMIT = 40 # normally 90sec
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

# Text constants
RED = pygame.Color("red")
GREEN = pygame.Color("green")
BLACK = pygame.Color("black")
ORANGE = pygame.Color("orange")
YELLOW = pygame.Color("yellow")

# Init pygame
pygame.init()
font = pygame.font.SysFont("comicsansms", 75)

# Init display
#display = pygame.display.set_mode((800, 600))
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.fill(BLACK)
pygame.display.set_caption('-- Ben ik KIH?! --')

# Clock init
clock = pygame.time.Clock()

# Read array from txt file
with open('/home/pi/Documents/Agame/wl.txt') as wl:
	wl_array = wl.readlines()

# Remove \n from wl_array
wl_array = [x.strip() for x in wl_array]

# Shuffle array
random.shuffle(wl_array)

# Main game loop 
def gameLoop():
	i = 0
	font = pygame.font.SysFont("comicsansms", 50) # epic may-may
	currentWord = font.render("Press mouse button to start", True, (0, 0, 0))
	display.blit(currentWord, (400 - currentWord.get_width() // 2, 300 - currentWord.get_height() // 2))
	font = pygame.font.SysFont("comicsansms", 75)
	pygame.display.flip()
	
	# Start new timer for a new round of fun
	timelimit = time.time() + 40 # 90s for full game
	
	# Guess words within time
	while time.time() < timelimit:
		display.fill(BLACK)
		currentWord = font.render(wl_array[i], True, GREEN)
		display.blit(currentWord, (400 - currentWord.get_width() // 2, 300 - currentWord.get_height() // 2))
		pygame.display.flip()
		
		# Clear event list
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.MOUSEBUTTONUP and i > len(wl_array):
				# Display new word
				#display.fill(BLACK)
				#currentWord = font.render(wl_array[i], True, GREEN)
				#display.blit(currentWord, (400 - currentWord.get_width() // 2, 300 - currentWord.get_height() // 2))
				i += 1
		
		time.sleep(.1)
    	pygame.display.flip()
    	clock.tick(60)
		
def endGame():
	display.fill(BLACK)
	currentWord = font.render("GAME OVER", True, RED)
	display.blit(currentWord, (400 - currentWord.get_width() // 2, 300 - currentWord.get_height() // 2))
	
	# new game?
	# yes no
	checkMouse()
#	mouse = pygame.mouse.get_pos()
	#if mouse is over button
# 	if 150+300 > mouse[0] > 150 and 400+50 > mouse[1] > 400:
# 		pygame.draw.rect(display, GREEN, (300, 400, 300, 50))
# 	else:
# 		pygame.draw.rect(display, ORANGE, (300, 400, 300, 50))

	#startOver text                                                                     
	currentWord = font.render("-- NewGame+? --", True, YELLOW)
	display.blit(currentWord, (300, 400, 300, 50))    #display new word

# Function to check for button activity
def checkMouse():
	mouse = pygame.mouse.get_pos()
	quitButton()
	newGamebutton()

# Quit button in the top right corner
def quitButton(mouse):
	if SCREEN_WIDTH - 50 > mouse[0] > SCREEN_WIDTH and 400+50 > mouse[1] > 400:
		pygame.draw.rect(display, GREEN, (SCREEN_WIDTH - 50, 0, 50, 50))
	else:
		pygame.draw.rect(display, ORANGE, (SCREEN_WIDTH - 50, 0, 50, 50))

# New game button in middle of screen at end of game
def newGameButton(mouse):
	if 150+300 > mouse[0] > 150 and 400+50 > mouse[1] > 400:
		pygame.draw.rect(display, GREEN, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 300, 50))
	else:
		pygame.draw.rect(display, ORANGE, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 300, 50))

# Rounds
still_want_to_play = True
while still_want_to_play:
	gameLoop()
	still_want_to_play = endGame()
