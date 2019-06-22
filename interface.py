import pygame
from pygame.locals import *
import time
import random


def pick_random_in_list(list_item):
	return list_item[random.randint(0,len(list_item)-1)]

#function to load a batch of screens 
def load_batch_images(*args,size_screen=(1058, 595)):
	return [pygame.transform.scale(pygame.image.load(arg),(1058, 595)) for arg in args]

#function to load a batch of sounds
def load_sounds(*args):
	sounds=[pygame.mixer.Sound(arg) for arg in args]
	return sounds
if __name__ == "__main__":
	pygame.init()
	#constants:
	#Size Screen
	size_screen=(1058, 595)

	#Sounds
	countdown_sound = load_sounds("sound_booth/countdown.ogg")[0]

	picture_sounds = load_sounds("sound_booth/camera-shutter1.ogg",
								"sound_booth/camera-shutter3.ogg",
								"sound_booth/camera-shutter8.ogg",
								"sound_booth/chinese-gong.ogg",
								"sound_booth/Cuckoo-clock.ogg",
								"sound_booth/party_horn.ogg")
	
	#Pictures
	welcomes = load_batch_images("picture_camera/ap_right.png",
								"picture_camera/ap.png",
								"picture_camera/ap_left.png",
								size_screen=size_screen)

	readies = load_batch_images("picture_camera/ready.png",
								size_screen=size_screen)

	#reverse count screens 
	screens_countdown = load_batch_images(*["count/image-000{:02}.png".format(i) for i in range(1,52)],
											size_screen=size_screen)

	#ending screens
	screens_ending = load_batch_images("picture_camera/end1.png",
										size_screen=size_screen)

	#opening window with black screen
	window = pygame.display.set_mode(size_screen,RESIZABLE)
	window.fill([0,0,0])
	pygame.display.flip()

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
				#displaying ready message
				countdown_sound.play()
				
				window.blit(pick_random_in_list(readies[0]),(0,0))
				pygame.display.flip()
				time.sleep(5)
				#erasing 
				window.fill([0,0,0])
				pygame.display.flip()
				
				for screen in screens_countdown:
					
					window.blit(screen,(0,0))
					pygame.display.flip()
					time.sleep(0.1)
				#take the picture here
				countdown_sound.stop()
				window.fill([0,0,0])
				pygame.display.flip()
				pick_random_in_list(picture_sounds).play()
				print("take the picture")

				#display random ending
				window.blit(pick_random_in_list(screens_ending),(0,0))
				pygame.display.flip()
				time.sleep(4)

				#displaying the welcome screen
				window.blit(welcomes[which_welcome_screen],(0,0))
				pygame.display.flip()

				#clearing the queue of events
				pygame.event.clear()
				break

		continue
	
