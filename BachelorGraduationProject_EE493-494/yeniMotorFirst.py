import time
import RPi.GPIO as GPIO
import board
import busio
import adafruit_vl53l0x
import polar2cart
import erase
import landmarkExtraction
import matplotlib
from matplotlib import pyplot as plt
    
def scan(robotLoc,pointCld,objMtx):

    DIR=27
    STEP=17
    SLEEP = 22
	
    CW=1
    CCW=0
    SPR=200 #Steps per revolution

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR,GPIO.OUT)
    GPIO.setup(STEP,GPIO.OUT)
    GPIO.setup(SLEEP, GPIO.OUT)
    GPIO.output(DIR,CW)

    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_vl53l0x.VL53L0X(i2c)

    liste=[]
    step_count=SPR
    delay=0.0208
    GPIO.output(SLEEP,GPIO.HIGH)

    for x in range(step_count):
	    GPIO.output(STEP,GPIO.HIGH)
	    time.sleep(delay)
	    GPIO.output(STEP,GPIO.LOW)
	    mes=format(sensor.range)
	    mes=int(mes)
#	    print(mes ,x*1.8)
	    liste.append([mes,(x*1.8)+robotLoc[2]]) # polar coordinat tutuyor
	    time.sleep(delay)
    
    	
    time.sleep(delay)
    GPIO.output(DIR,CCW)

    for x in range(step_count):
	    GPIO.output(STEP,GPIO.HIGH)
	    time.sleep(delay)
	    mes=format(sensor.range)
	    mes=int(mes)
#	    print(mes ,x)
	    liste.append([mes,(358.2-(x*1.8)+robotLoc[2])]) # polar coordinat tutuyor
	    GPIO.output(STEP,GPIO.LOW)
	    time.sleep(delay)

    polarRr=[]
    for pp in range(0,200):
	    polarRr.append([((liste[pp][0])+(liste[399-pp][0]))/2, liste[pp][1]])
    
    GPIO.output(SLEEP,GPIO.LOW)
    GPIO.output(STEP,GPIO.LOW)
    #GPIO.output(DIR,GPIO.LOW)
    GPIO.cleanup()
    cartListe2=polar2cart.polar2cart(robotLoc,polarRr)  ##Cartliste filtrele
    
    filteredList2=erase.morp(cartListe2)
    filtered=filteredList2
    xler=[]
    yler=[]
    for i in filtered:
        xler.append(i[0])
        yler.append(i[1])
    
   # plt.scatter(xler,yler)
    freshObjMtx=landmarkExtraction.landmarkExtraction(robotLoc,filtered,objMtx)
 #   print('freshObjMtx=',freshObjMtx)
    
    filtered=pointCld+filtered
 #   print('filtered=',filtered)
    return [filtered,freshObjMtx]
