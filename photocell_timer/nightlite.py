#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

IO_LED = 25
GPIO.setup(IO_LED, GPIO.OUT)

ledState = False

def resistorTimerReading(ioPort):
	reading = 0

	GPIO.setup(ioPort, GPIO.OUT)
	GPIO.output(ioPort, GPIO.LOW)

	sleep(0.1)

	GPIO.setup(ioPort, GPIO.IN)
	while GPIO.input(ioPort) == GPIO.LOW:
		reading += 1

	return reading

while True:
	lightLevel = resistorTimerReading(18)
	if lightLevel >= 800:
		previousLedState = ledState
		ledState = True

		if previousLedState is False:
			print "It's dark!"
			GPIO.output(IO_LED, True)
	else:
		previousLedState = ledState
		ledState = False

		if previousLedState:
			print 'Finally, I can see again!'
			GPIO.output(IO_LED, False)