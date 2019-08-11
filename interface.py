import pygame
from pygame.locals import *
import time
import random
from picture_manager import PictureManager


class Interface():

	def __init__(self, size_screen, countdown_sound, shots_sounds, welcome_imgs, readies, screens_countdown, screens_ending, preview_screens, save_folder):
		pygame.init()
		# screens and sounds
		self.size_screen = size_screen
		self.countdown_sound = self.load_sounds(countdown_sound)[0]
		self.shots_sounds = self.load_sounds(*shots_sounds)
		self.welcome_imgs = self.load_images(*welcome_imgs)
		self.which_welcome_screen = 1
		self.readies = self.load_images(*readies)
		self.screens_countdown = self.load_images(*screens_countdown)
		self.screens_ending = self.load_images(*screens_ending)
		self.preview_screens = self.load_images(*preview_screens)

		# Camera folder and pictures
		self.save_folder = save_folder
		self.camera = PictureManager()
		self.count_photo = 0

		# Start displaying
		self.window = pygame.display.set_mode((0, 0), FULLSCREEN)
		self.window.fill([0, 0, 0])
		pygame.display.flip()
		self.window.blit(self.welcome_imgs[1], (0, 0))
		pygame.display.flip()

	def load_images(self, *args):
		return [pygame.transform.scale(pygame.image.load(arg), self.size_screen) for arg in args]

	def load_sounds(self, *args):
		return [pygame.mixer.Sound(arg) for arg in args]

	def welcome_screen(self):
		time.sleep(1)
		if self.which_welcome_screen == 1:
			self.which_welcome_screen = random.randint(0, 1) * 2
		elif self.which_welcome_screen == 2 or self.which_welcome_screen == 0:
			self.which_welcome_screen = 1 
		# displaying switching screen
		self.window.blit(self.welcome_imgs[self.which_welcome_screen], (0, 0))
		pygame.display.flip()

	def play_countdown(self):
		# play sound
		self.countdown_sound.play()
		# displaying ready message for 5 seconds
		self.window.blit(pick_random_in_list(self.readies), (0, 0))
		pygame.display.flip()
		time.sleep(5)
		
		# countdown
		for screen in self.screens_countdown:
			
			self.window.blit(screen, (0, 0))
			pygame.display.flip()
			time.sleep(0.1)

		self.countdown_sound.stop()
		# filling black the window
		self.window.fill([0, 0, 0])
		pygame.display.flip()

	def play_ending(self):
		# choosing random ending in the list
		self.window.blit(pick_random_in_list(self.screens_ending), (0, 0))
		pygame.display.flip()
		time.sleep(4)

	def take_picture(self, **kwargs):
		self.camera.take_picture(self.save_folder + "photo_{:05d}".format(self.count_photo) + ".jpg", sleeptime=2.5, action_func=pick_random_in_list(self.shots_sounds).play)
		self.count_photo += 1

	def display_picture(self, index, delay=6):
		self.window.blit(pick_random_in_list(self.preview_screens), (0, 0))
		real_index = range(self.count_photo)[index]
		img = self.load_images("photo_{:05d}".format(real_index) + ".jpg")[0]
		self.window.blit(img, (0, 0))
		pygame.display.flip()
		time.sleep(delay)


def pick_random_in_list(list_item):
	return list_item[random.randint(0, len(list_item) - 1)]

	return sounds


if __name__ == "__main__":
	
	# constants:
	# Size Screen
	size_screen = (650, 500)

	countdown_sound = "sound_booth/countdown.ogg"

	shots_sounds = ["sound_booth/camera-shutter1.ogg",
				  "sound_booth/camera-shutter3.ogg",
				  "sound_booth/camera-shutter8.ogg",
				  "sound_booth/chinese-gong.ogg",
				  "sound_booth/Cuckoo-clock.ogg",
				  "sound_booth/party_horn.ogg"]

	welcome_imgs = ["picture_camera/ap_right.png",
				  "picture_camera/ap.png",
				  "picture_camera/ap_left.png"]

	readies = ["picture_camera/ready.png"]

	screens_countdown = ["count/image-000{:02}.png".format(i) for i in range(1, 52)]

	screens_ending = ["picture_camera/end" + str(integer) + ".png" for integer in range(1, 6)]

	preview_screens = ["picture_camera/preview.png",
					   "picture_camera/preview2.png"]

	save_folder = "/home/pi/Pictures/image_taken/"

	interface = Interface(size_screen, countdown_sound, shots_sounds, welcome_imgs, readies, screens_countdown, screens_ending, preview_screens, save_folder)

	keep_open = True
	# tracker for which screen is currently running
	while keep_open:

		# make the camera flip
		interface.welcome_screen()

		# Dealing with events in this loop
		for event in pygame.event.get():

			# Quit event for exiting the window
			if event.type == QUIT:
				keep_open = False

			# Event when clicking
			if event.type == MOUSEBUTTONDOWN:
				interface.play_countdown()

				interface.take_picture()

				# display random ending
				interface.play_ending()

				# display preview picture (index -1 refers to the last picture)
				interface.display_picture(-1)

				# display welcome screen
				interface.welcome_screen()

				# clearing the queue of events
				pygame.event.clear()
				break

		continue
	
