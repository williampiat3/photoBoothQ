import pygame
from pygame.locals import *
import time
import random

#function to load a batch of screens 
def load_batch_images(*args):
	return [pygame.image.load(arg) for arg in args]
if __name__ == "__main__":
	pygame.init()
	#opening window
	window = pygame.display.set_mode((1058, 595),RESIZABLE)
	window.fill([255,255,255])
	pygame.display.flip()
	#loading different screens 
	welcomes = load_batch_images("Sans nom ap right.jpg","Sans nom ap.jpg","Sans nom ap left.jpg")
	

	#reverse count screens 
	screens_countdown = load_batch_images(*["count/image-000{:02}.png".format(i) for i in range(1,52)])

	#ending screens
	screens_ending = load_batch_images("Sans nom ending1.jpg")

	#setting first screen as the centered one
	window.blit(welcomes[1],(0,0))
	pygame.display.flip()

	keep_open = True
	#tracker for which screen is currently running
	which_welcome_screen=1
	#Main loop for running the program
	while keep_open:

		#make the camera flip
		time.sleep(1)
		if which_welcome_screen==1:
			which_welcome_screen=random.randint(0,1)*2
		elif which_welcome_screen==2 or which_welcome_screen==0:
			which_welcome_screen=1 
		#displaying switching screen
		window.blit(welcomes[which_welcome_screen],(0,0))
		pygame.display.flip()


		#Dealing with events in this loop
		for event in pygame.event.get():

			#quit event for exiting the window
			if event.type == QUIT:
				keep_open = False

			#Event when clicking
			if event.type == MOUSEBUTTONDOWN:
				window.fill([0,0,0])
				pygame.display.flip()
				for screen in screens_countdown:

					window.blit(screen,(-90,-30))
					pygame.display.flip()
					time.sleep(0.05)
				#take the picture here
				time.sleep(2)
				print("take the picture")

				#display random ending
				window.blit(screens_ending[random.randint(0,len(screens_ending)-1)],(0,0))
				pygame.display.flip()
				time.sleep(4)

				#displaying the welcome screen
				window.blit(welcomes[which_welcome_screen],(0,0))
				pygame.display.flip()

				#clearing the queue of events
				pygame.event.clear()
				break

		continue
	
