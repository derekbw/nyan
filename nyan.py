import time
import pygame
import RPi.GPIO as io
import random
io.setmode(io.BCM)

pir_pin = 18

io.setup(pir_pin, io.IN)
print("initializing...")
pygame.mixer.init()
print("initialized")
print("loading file...")
#pygame.mixer.music.load("nyan.mp3")
print("file loaded")
pygame.mixer.music.set_volume(1.0)
nyans = [ "nyan.mp3", "nyanorchestra.mp3", "nyanwaits.mp3", "nyanjazz.mp3" ]

while True:
	if io.input(pir_pin):
		if pygame.mixer.music.get_busy() == False:
			rand = random.randint(0, 3)
			pygame.mixer.music.load(nyans[rand])
			pygame.mixer.music.play()	
			print("starting " + nyans[rand])
#	time.sleep(0.5)
