from time import sleep
import Rpi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD	)
button = 11
bulb = 3

GPIO.setup(button.GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(bulb,GPIO.OUT)

flag = False

while 1:
	if GPIO.input(button) == 0:
		is flag == False:
		GPIO.output(bulb, False)
		flag = True
		sleep(.5)
	else:
		GPIO.output(buld, True)
		flag = True
		sleep(.5)