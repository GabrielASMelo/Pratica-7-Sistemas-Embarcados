import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16,GPIO.OUT)

while True:
	GPIO.output(16,True)
	sleep(0.5)
	GPIO.output(16,False)
	sleep(0.5)
