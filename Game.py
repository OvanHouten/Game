#!/usr/bin/python


#import shit;
import os
import sys
import random

from termcolor import cprint 
from pyfiglet import figlet_format

print "Let the game begin!"

#INIT SHIT
wl_array = []

#read wl in array
with open('../wl.txt') as wl:
	wl_array = wl.readlines()

#remove \n
wl_array = [x.strip() for x in wl_array]

#shuffle array
random.shuffle(wl_array)

#print array
for woord in wl_array:
	#clear screen
	os.system('clear')

	#print woord in banner
	cprint(figlet_format(woord, font='starwars'),'yellow', 'on_green', attrs=['bold'])

	#wacht op user in put
	raw_input('Druk op `ENTER` voor volgend woord (CNTRL + C to quit)')

	#clear screen
	os.system('clear')
