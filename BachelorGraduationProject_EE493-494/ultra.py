import RPi.GPIO as GPIO
import time
 


def distance(side):
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False) 
	 
	#GPIO Pins
	GPIO_TRIGGER_R = 11
	GPIO_ECHO_R = 9
	GPIO_TRIGGER_F = 25
	GPIO_ECHO_F = 5
	GPIO_TRIGGER_L = 18
	GPIO_ECHO_L = 4
	 
	GPIO.setup(GPIO_TRIGGER_F, GPIO.OUT)
	GPIO.setup(GPIO_ECHO_F, GPIO.IN)
	GPIO.setup(GPIO_TRIGGER_R, GPIO.OUT)
	GPIO.setup(GPIO_ECHO_R, GPIO.IN)
	GPIO.setup(GPIO_TRIGGER_L, GPIO.OUT)
	GPIO.setup(GPIO_ECHO_L, GPIO.IN) 

	if (side ==0 ):	#front
		#GPIO.output(GPIO_TRIGGER_F, False)
		#time.sleep(0.00001)
		print('check front') 
		GPIO.output(GPIO_TRIGGER_F,True)
		time.sleep(0.00001)
		GPIO.output(GPIO_TRIGGER_F, False)

		StartTime = time.time()
		StopTime = time.time()

		while GPIO.input(GPIO_ECHO_F) == 0:
			StartTime = time.time()

		while GPIO.input(GPIO_ECHO_F) == 1:
			StopTime = time.time()

		TimeElapsed = StopTime - StartTime
		#sound speed 34300 cm/s forth and back
		distance = (TimeElapsed * 34300) / 2
	
	elif (side == 1):	#right
		#GPIO.output(GPIO_TRIGGER_R, False)
		#time.sleep(0.00001)
		print('check right') 
		GPIO.output(GPIO_TRIGGER_R, True)
		time.sleep(0.00001)
		GPIO.output(GPIO_TRIGGER_R, False)

		StartTime = time.time()
		StopTime = time.time()

		while GPIO.input(GPIO_ECHO_R) == 0:
			StartTime = time.time()

		while GPIO.input(GPIO_ECHO_R) == 1:
			StopTime = time.time()

		TimeElapsed = StopTime - StartTime
		#sound speed 34300 cm/s forth and back
		distance = (TimeElapsed * 34300) / 2
	
	elif (side == -1):	#left
		GPIO.output(GPIO_TRIGGER_L, False)
		time.sleep(0.00001)
		GPIO.output(GPIO_TRIGGER_L, True)
		time.sleep(0.00001)
		GPIO.output(GPIO_TRIGGER_L, False)

		StartTime = time.time()
		StopTime = time.time()

		while GPIO.input(GPIO_ECHO_L) == 0:
			StartTime = time.time()
			
		while GPIO.input(GPIO_ECHO_L) == 1:
			StopTime = time.time()

		TimeElapsed = StopTime - StartTime
		#sound speed 34300 cm/s forth and back
		distance = (TimeElapsed * 34300) / 2

	return distance
