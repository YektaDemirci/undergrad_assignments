import time
import encoderemre
import copy
import csv
import threading
import yeniMotor
import ultra

def Clockwise(cap,pointCld,RobotLoc,ObjMtx,oldXY):   
    count=0

    #First scan
    pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
    time.sleep(0.01)    

    if(ultra.distance(-1)<20): #check left
        time.sleep(0.01)
        return count,pointCld,RobotLoc,ObjMtx,oldXY 
    
    RobotLoc=encoderemre.gtime(RobotLoc,90,0)#turn left
    time.sleep(0.01)
    RobotLoc=encoderemre.gtime(RobotLoc,0,cap)#go straight
    count=1
    time.sleep(0.01)

    if(ultra.distance(1)<20): #check right
        return count,pointCld,RobotLoc,ObjMtx,oldXY 

    RobotLoc=encoderemre.gtime(RobotLoc,-90,0)#turn right
    time.sleep(0.01)
    RobotLoc=encoderemre.gtime(RobotLoc,0,cap)#go straight
    time.sleep(0.01)

    count=2
    time.sleep(0.01)

    #Second scan
    pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
    time.sleep(0.01)
    
    if(ultra.distance(0)<20 and False):#check front
        return count,pointCld,RobotLoc,ObjMtx,oldXY #gideceği istikameti kontrol ediyor distance checkler hep 90lık dönüşlerden sonra
    
    RobotLoc=encoderemre.gtime(RobotLoc,0,cap)#go straight
    time.sleep(0.1)

    count=3
    
    if(ultra.distance(1)<20):#check right
        return count,pointCld,RobotLoc,ObjMtx,oldXY

    RobotLoc=encoderemre.gtime(RobotLoc,-90,0)#turn right
    time.sleep(0.1)
    RobotLoc=encoderemre.gtime(RobotLoc,0,cap)#go straight
    time.sleep(0.1)

    count=4
    time.sleep(0.01)

    #Third scan
    pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
    time.sleep(0.01)
  
    if(ultra.distance(0)<20):#check front BURASI 1 OLABİLİR
        return count,pointCld,RobotLoc,ObjMtx,oldXY

    RobotLoc=encoderemre.gtime(RobotLoc,0,cap)#go straight
    time.sleep(0.01)

    count=5
    time.sleep(0.01)
    
    
    if(ultra.distance(1)<20):#check right
        return count,pointCld,RobotLoc,ObjMtx,oldXY
   
    RobotLoc=encoderemre.gtime(RobotLoc,-90,0)#turn right
    time.sleep(0.01)
    RobotLoc=encoderemre.gtime(RobotLoc,0,cap)#go straight
    time.sleep(0.01)

    count=6
    time.sleep(0.01)      

    #Final scan
    pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
    time.sleep(0.01)
    
    return count,pointCld,RobotLoc,ObjMtx,oldXY


