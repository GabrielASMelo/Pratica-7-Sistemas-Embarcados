#!/bin/bash

echo 23 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio23/direction

while [ 1 ]
	do
		echo 1 > /sys/class/gpio/gpio23/value
		sleep 0.2s
		echo 0 > /sys/class/gpio/gpio23/value
		sleep 0.2s
	done

# Gabriel Aguilar Soares de Melo 11915432
# João Pedro Suzuki de Figueiredo 11800712
