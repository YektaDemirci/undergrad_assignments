import RPi.GPIO as GPIO
from gpiozero import PWMOutputDevice
import time
import csv
import math
def gtime(robotLoc,rotation,distance):
    A_pin = 24
    B_pin = 23
    C_pin = 6
    D_pin = 13
    
    PWMPin1 = 16 # PWM Pin connected to ENA. bunlar hep board
    Motor1 = 20 # Connected to Input 1.
    Motor2 = 21 # Connected to Input 2.
    
    PWMPin2= 12 # PWM Pin connected to ENA. bunlar hep board
    Motor3 = 26 # Connected to Input 1.
    Motor4 = 19 # Connected to Input 2.
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(A_pin, GPIO.IN)
    GPIO.setup(B_pin, GPIO.IN)
    GPIO.setup(C_pin, GPIO.IN)
    GPIO.setup(D_pin, GPIO.IN)
    
    
    GPIO.setwarnings(False)
    
    GPIO.setup(PWMPin1, GPIO.OUT)
    GPIO.setup(PWMPin2, GPIO.OUT) # We have set our pin mode to output
    GPIO.setup(Motor1, GPIO.OUT)
    GPIO.setup(Motor2, GPIO.OUT)
    GPIO.setup(Motor3, GPIO.OUT)
    GPIO.setup(Motor4, GPIO.OUT)
     
    GPIO.output(PWMPin1, GPIO.LOW) 
    GPIO.output(PWMPin2, GPIO.LOW) 
    GPIO.output(Motor1, GPIO.LOW)
    GPIO.output(Motor2, GPIO.LOW)
    GPIO.output(Motor3, GPIO.LOW)
    GPIO.output(Motor4, GPIO.LOW)
    
     
    PwmValue1 = GPIO.PWM(PWMPin1, 50) # We have set our PWM frequency to 2000.
    PwmValue1.start(0) # That's the maximum value 100 %.
    PwmValue2 = GPIO.PWM(PWMPin2, 50) # We have set our PWM frequency to 2000.
    PwmValue2.start(0) # That's the maximum value 100 %.
    
    outcome = [0, -1, 1, 0, -1 ,0 ,0, 1 ,1 ,0 ,0 , -1, 0, -1 ,1 ,0]
    last_AB = 0b00
    last_CD = 0b00
    counterAB = 0
    counterCD = 0
    #def move(rotation,distance):
    sumerr2=0
    sumerr1=0
    err1=0
    err2=0
    
    #cansu editi

    R_avg = 8.45 #cm
    C_avg =2*math.pi*R_avg#2piR
    C_wheel =11.16 
    n = 823.1*2
    count_per_angle = (C_avg/C_wheel)*n/360
    count_per_cm = n/C_wheel
    #sanki bi şeyle daha çarpıcaz ama bilemedim
    # Robotun 1 tur dönmesi --> 4.46 tur tekerlek dönmesi
    #Açı başına sayım sayısı = (4.46/360*angle)*n -->n 11 ya da 22 ??
    
    if(rotation!=0):
        desiredCnt1=round(float(rotation)*count_per_angle)
        desiredCnt2=desiredCnt1*(-1)
    
    else:
        desiredCnt1=round(float(distance)*count_per_cm) 
        desiredCnt2=desiredCnt1*(1)
    
    Kp=0.72*100
    Ki=0.26*100
    errc=9000
    #print(desiredCnt1,desiredCnt2)
    
    contAr1=[0,1]
    contAr2=[0,1]
    flag=0
    strt=0
    while True:
    
        err1=desiredCnt1-counterAB
        err2=desiredCnt2-counterCD
    	
        contAr1[0]=contAr1[1]
        contAr1[1]=err1
    	
        contAr2[0]=contAr2[1]
        contAr2[1]=err2
        
        if((abs(err1)<20 and abs(err2)<20) and flag==0):
            tout=0.2
            flag=1
            strt=time.time()
            if(abs(err1)<5 and abs(err2)<5):
                GPIO.output(Motor2, GPIO.LOW)
                GPIO.output(Motor1, GPIO.LOW)
                GPIO.output(Motor3, GPIO.LOW)
                GPIO.output(Motor4, GPIO.LOW)
                GPIO.cleanup()
            
        elif((abs(err1)<15 and abs(err2)<15) and flag==1):
            if(time.time()>strt+tout):
                
                GPIO.output(Motor2, GPIO.LOW)
                GPIO.output(Motor1, GPIO.LOW)
                GPIO.output(Motor3, GPIO.LOW)
                GPIO.output(Motor4, GPIO.LOW)
                GPIO.cleanup() ## yeni rotation ve distance üzerinden konum döndür
                
                robotLoc[2]=(robotLoc[2]+actual_rotation)
                robotLoc[0]=robotLoc[0]+(actual_distance*math.cos(math.radians(robotLoc[2])))*10
                robotLoc[1]=robotLoc[1]+(actual_distance*math.sin(math.radians(robotLoc[2])))*10

                return robotLoc			
        else:
            tout=0
            flag=0 
                   
 #       if (contAr1[0]==contAr1[1]) and (contAr2[0]==contAr2[1]):
  #          if counterAB and abs(m1speed)<1:

    	          
        if err1>0 and err2>0:
            GPIO.output(Motor2, GPIO.HIGH)
            GPIO.output(Motor1, GPIO.LOW)
            GPIO.output(Motor3, GPIO.HIGH)
            GPIO.output(Motor4, GPIO.LOW)
    	    
        elif err1<0 and err2<0:
    
            GPIO.output(Motor2, GPIO.LOW)
            GPIO.output(Motor1, GPIO.HIGH)
            GPIO.output(Motor3, GPIO.LOW)
            GPIO.output(Motor4, GPIO.HIGH)
    	    
    	    
        elif err1<0 and err2>0:
    
            GPIO.output(Motor2, GPIO.LOW)
            GPIO.output(Motor1, GPIO.HIGH)
            GPIO.output(Motor3, GPIO.HIGH)
            GPIO.output(Motor4, GPIO.LOW)
    	    
    	    
        elif err1>0 and err2<0:
    
            GPIO.output(Motor2, GPIO.HIGH)
            GPIO.output(Motor1, GPIO.LOW)
            GPIO.output(Motor3, GPIO.LOW)
            GPIO.output(Motor4, GPIO.HIGH)
    	
    	    
        A = GPIO.input(A_pin)
        B = GPIO.input(B_pin)
        C = GPIO.input(C_pin)
        D = GPIO.input(D_pin)
    
        current_AB = (A << 1 ) | B
        positionAB = (last_AB << 2) | current_AB
        counterAB += outcome[positionAB]
        last_AB = current_AB
    	    
        current_CD = (C << 1 ) | D
        positionCD= (last_CD << 2) | current_CD
        counterCD += outcome[positionCD]
        last_CD = current_CD
    
      #  time.sleep(0.000001)
        actual_distance = ((counterAB+counterCD)/2)/n*C_wheel #cm
        actual_rotation = ((counterAB-counterCD)/2)/n*360*C_wheel/C_avg
    
        sumerr1+=err1
        sumerr2+=err2
    
        if(sumerr1>errc):
            sumerr1=errc
        if(sumerr2>errc):
            sumerr2=errc
        if(sumerr1<-errc):
            sumerr1=-errc
        if(sumerr2<-errc):
            sumerr2=-errc
     
    	    
        m1speed=(abs(err1/desiredCnt1))*Kp+(abs(sumerr1/desiredCnt1))*Ki
        m2speed=(abs(err2/desiredCnt2))*Kp+(abs(sumerr2/desiredCnt2))*Ki
       # print(err1,err2)	    

        if(m1speed>80):
            m1speed=80
        if(m2speed>80):
            m2speed=80		
    	
        PwmValue1.ChangeDutyCycle(m1speed)
        PwmValue2.ChangeDutyCycle(m2speed)
        

def gosh(robotLoc,pathList):
    import math
    
    for dest in pathList:
        
        distance = math.sqrt(((dest[0]-robotLoc[0])**2)+((dest[1]-robotLoc[1])**2))
        rotation = math.atan2((dest[1]-robotLoc[1]),(dest[0]-robotLoc[0]))
        rotation = math.degrees(rotation)-robotLoc[2]
        if abs(rotation) > 3:
            print(rotation)
            robotLoc=gtime(robotLoc,rotation,0)
        if abs (distance) > 10:
            print(distance)
            robotLoc=gtime(robotLoc,0,distance/10)
    return robotLoc



'''
import RPi.GPIO as GPIO
from gpiozero import PWMOutputDevice
import time
import csv
import math
def gtime(robotLoc,rotation,distance):
    A_pin = 24
    B_pin = 23
    C_pin = 6
    D_pin = 13
    
    PWMPin1 = 16 # PWM Pin connected to ENA. bunlar hep board
    Motor1 = 20 # Connected to Input 1.
    Motor2 = 21 # Connected to Input 2.
    
    PWMPin2= 12 # PWM Pin connected to ENA. bunlar hep board
    Motor3 = 26 # Connected to Input 1.
    Motor4 = 19 # Connected to Input 2.
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(A_pin, GPIO.IN)
    GPIO.setup(B_pin, GPIO.IN)
    GPIO.setup(C_pin, GPIO.IN)
    GPIO.setup(D_pin, GPIO.IN)
    
    
    GPIO.setwarnings(False)
    
    GPIO.setup(PWMPin1, GPIO.OUT)
    GPIO.setup(PWMPin2, GPIO.OUT) # We have set our pin mode to output
    GPIO.setup(Motor1, GPIO.OUT)
    GPIO.setup(Motor2, GPIO.OUT)
    GPIO.setup(Motor3, GPIO.OUT)
    GPIO.setup(Motor4, GPIO.OUT)
     
    GPIO.output(PWMPin1, GPIO.LOW) 
    GPIO.output(PWMPin2, GPIO.LOW) 
    GPIO.output(Motor1, GPIO.LOW)
    GPIO.output(Motor2, GPIO.LOW)
    GPIO.output(Motor3, GPIO.LOW)
    GPIO.output(Motor4, GPIO.LOW)
    
     
    PwmValue1 = GPIO.PWM(PWMPin1, 50) # We have set our PWM frequency to 2000.
    PwmValue1.start(0) # That's the maximum value 100 %.
    PwmValue2 = GPIO.PWM(PWMPin2, 50) # We have set our PWM frequency to 2000.
    PwmValue2.start(0) # That's the maximum value 100 %.
    
    outcome = [0, -1, 1, 0, -1 ,0 ,0, 1 ,1 ,0 ,0 , -1, 0, -1 ,1 ,0]
    last_AB = 0b00
    last_CD = 0b00
    counterAB = 0
    counterCD = 0
    #def move(rotation,distance):
    sumerr2=0
    sumerr1=0
    err1=0
    err2=0
    
    #cansu editi
    R_avg = 8.8 #cm
    C_avg = 58.985#2piR
    C_wheel = 12.4
    n = 823.1*2
    count_per_angle = (C_avg/C_wheel)*n/360
    count_per_cm = n/C_wheel
    #sanki bi şeyle daha çarpıcaz ama bilemedim
    # Robotun 1 tur dönmesi --> 4.46 tur tekerlek dönmesi
    #Açı başına sayım sayısı = (4.46/360*angle)*n -->n 11 ya da 22 ??
    
    if(rotation!=0):
        desiredCnt1=round(float(rotation)*count_per_angle)
        desiredCnt2=desiredCnt1*(-1)
    
    else:
        desiredCnt1=round(float(distance)*count_per_cm) 
        desiredCnt2=desiredCnt1*(1)
    
    Kp=0.72*100
    Ki=0.26*100
    errc=9000
    #print(desiredCnt1,desiredCnt2)
    
    contAr1=[0,1]
    contAr2=[0,1]
    flag=0
    strt=0
    while True:
    
        err1=desiredCnt1-counterAB
        err2=desiredCnt2-counterCD
    	
        contAr1[0]=contAr1[1]
        contAr1[1]=err1
    	
        contAr2[0]=contAr2[1]
        contAr2[1]=err2
        
        if((abs(err1)<15 and abs(err2)<15) and flag==0):
            tout=0.2
            flag=1
            strt=time.time()
            if(abs(err1)<5 and abs(err2)<5):
                GPIO.output(Motor2, GPIO.LOW)
                GPIO.output(Motor1, GPIO.LOW)
                GPIO.output(Motor3, GPIO.LOW)
                GPIO.output(Motor4, GPIO.LOW)
                GPIO.cleanup()
            
        elif((abs(err1)<20 and abs(err2)<20) and flag==1):
            if(time.time()>strt+tout):
                
                GPIO.output(Motor2, GPIO.LOW)
                GPIO.output(Motor1, GPIO.LOW)
                GPIO.output(Motor3, GPIO.LOW)
                GPIO.output(Motor4, GPIO.LOW)
                GPIO.cleanup() ## yeni rotation ve distance üzerinden konum döndür

                robotLoc[0]=robotLoc[0]+actual_distance*math.cos(math.radians(robotLoc[2]))
                robotLoc[1]=robotLoc[1]+actual_distance*math.sin(math.radians(robotLoc[2]))
                robotLoc[2]=robotLoc[2]+actual_rotation
                return robotLoc			
        else:
            tout=0
            flag=0 
                   
 #       if (contAr1[0]==contAr1[1]) and (contAr2[0]==contAr2[1]):
  #          if counterAB and abs(m1speed)<1:

    	          
        if err1>0 and err2>0:
            GPIO.output(Motor2, GPIO.HIGH)
            GPIO.output(Motor1, GPIO.LOW)
            GPIO.output(Motor3, GPIO.HIGH)
            GPIO.output(Motor4, GPIO.LOW)
    	    
        elif err1<0 and err2<0:
    
            GPIO.output(Motor2, GPIO.LOW)
            GPIO.output(Motor1, GPIO.HIGH)
            GPIO.output(Motor3, GPIO.LOW)
            GPIO.output(Motor4, GPIO.HIGH)
    	    
    	    
        elif err1<0 and err2>0:
    
            GPIO.output(Motor2, GPIO.LOW)
            GPIO.output(Motor1, GPIO.HIGH)
            GPIO.output(Motor3, GPIO.HIGH)
            GPIO.output(Motor4, GPIO.LOW)
    	    
    	    
        elif err1>0 and err2<0:
    
            GPIO.output(Motor2, GPIO.HIGH)
            GPIO.output(Motor1, GPIO.LOW)
            GPIO.output(Motor3, GPIO.LOW)
            GPIO.output(Motor4, GPIO.HIGH)
    	
    	    
        A = GPIO.input(A_pin)
        B = GPIO.input(B_pin)
        C = GPIO.input(C_pin)
        D = GPIO.input(D_pin)
    
        current_AB = (A << 1 ) | B
        positionAB = (last_AB << 2) | current_AB
        counterAB += outcome[positionAB]
        last_AB = current_AB
    	    
        current_CD = (C << 1 ) | D
        positionCD= (last_CD << 2) | current_CD
        counterCD += outcome[positionCD]
        last_CD = current_CD
    
      #  time.sleep(0.000001)
        actual_distance = ((counterAB+counterCD)/2)/n*C_wheel #cm
        actual_rotation = ((counterAB-counterCD)/2)/n*360*C_wheel/C_avg
    
        sumerr1+=err1
        sumerr2+=err2
    
        if(sumerr1>errc):
            sumerr1=errc
        if(sumerr2>errc):
            sumerr2=errc
        if(sumerr1<-errc):
            sumerr1=-errc
        if(sumerr2<-errc):
            sumerr2=-errc
     
    	    
        m1speed=(abs(err1/desiredCnt1))*Kp+(abs(sumerr1/desiredCnt1))*Ki
        m2speed=(abs(err2/desiredCnt2))*Kp+(abs(sumerr2/desiredCnt2))*Ki
        print(err1,err2)	    

        if(m1speed>80):
            m1speed=80
        if(m2speed>80):
            m2speed=80		
    	
        PwmValue1.ChangeDutyCycle(m1speed)
        PwmValue2.ChangeDutyCycle(m2speed)
        

def gosh(robotLoc,pathList):
    import math
    
    for dest in pathList:
        
        distance = math.sqrt(((dest[0]-robotLoc[0])**2)+((dest[1]-robotLoc[1])**2))
        rotation = math.atan2((dest[1]-robotLoc[1]),(dest[0]-robotLoc[0]))
        rotation = math.degrees(rotation)-robotLoc[2]
        if abs(rotation) > 3:
            robotLoc=gtime(robotLoc,rotation,0)
        if abs (distance) > 10:
            robotLoc=gtime(robotLoc,0,distance/10)
    return robotLoc
'''
