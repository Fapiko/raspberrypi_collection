#!/bin/bash

for i in {23..25}
do
	#echo "$i" > /sys/class/gpio/export
	#echo "in" > /sys/class/gpio/gpio$i/direction
	cat /sys/class/gpio/gpio$i/value
done

