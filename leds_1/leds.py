#!/usr/bin/env python

import RPi.GPIO as GPIO, time

def main():
	GPIO.setmode(GPIO.BCM)
	GREEN_LED = 18
	BLUE_LED = 17
	RED_LED = 23
	GPIO.setup(GREEN_LED, GPIO.OUT)
	GPIO.setup(BLUE_LED, GPIO.OUT)
	GPIO.setup(RED_LED, GPIO.OUT)

	timer = 0

	GPIO.output(BLUE_LED, GP)
	while True:

		print timer

		if timer % 2:
			GPIO.output(GREEN_LED, False)
			GPIO.output(RED_LED, True)

		if timer % 5:
			GPIO.output(GREEN_LED, True)
			GPIO.output(RED_LED, False)

		if timer % 10:
			GPIO.output(GREEN_LED, True)
			GPIO.output(RED_LED, True)

		timer += 1

		time.sleep(1)

try:
	main()
except KeyboardInterrupt:
	print 'Exiting...'
	GPIO.cleanup
