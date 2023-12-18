import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
#desativa avisos 
GPIO.setmode(GPIO.BOARD)
#coloca a GPIO chamando os pinos de acordo com o número do PINO!
GPIO.setup(16,GPIO.OUT)
#coloca o pino conectado no circuito do led como pino de saída
while True:
	GPIO.output(16,True)
	sleep(0.5)
	GPIO.output(16,False)
	sleep(0.5)
# while permite uma repetição contínua da ativação e desativação do pino, num periodo de 0,5s

# Gabriel Aguilar Soares de Melo 11915432
# João Pedro Suzuki de Figueiredo 11800712
