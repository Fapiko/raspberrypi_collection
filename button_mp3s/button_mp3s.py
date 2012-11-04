#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

buttonStates = dict()

# Setup loop
for i in range(23, 26):
	GPIO.setup(i, GPIO.IN)
	buttonStates[i] = False

ghettoTimer = 0
while True:
	for i in range(23, 26):
		if GPIO.input(i) is False:
			previousState = buttonStates[i]
			buttonStates[i] = True

			if previousState is False:
				print "%d down" % (i)

		else:
			previousState = buttonStates[i]
			buttonStates[i] = False

			if previousState:
				print "%d up" % (i)

				if i == 23:
					os.system('killall mpg321; mpg321 "01 - Rain Is a Good Thing.mp3" &')
				elif i == 24:
					os.system('killall mpg321; mpg321 "02 - David Draiman of Disturbed - Forsaken.mp3" &')
				elif i == 25:
					os.system('killall mpg321; mpg321 "10 Awolnation - Sail.mp3" &')

	ghettoTimer += 1

	if ghettoTimer % 10 == 0:
		print ghettoTimer / 10

	sleep(.1);
