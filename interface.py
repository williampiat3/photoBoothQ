import pygame
from pygame.locals import *

if __name__ == "__main__":
	pygame.init()
	#opening window
	window = pygame.display.set_mode((640, 480),RESIZABLE)
	window.fill([255,255,255])
	pygame.display.flip()
	keep_open = True
	#Main loop for running the program
	while keep_open:
		for event in pygame.event.get():
			if event.type == QUIT:
				keep_open = False
			if event.type == KEYDOWN and  event.key == K_UP:
				print('up madafaka')

		continue
	
