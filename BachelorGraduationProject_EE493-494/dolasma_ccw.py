import time
import encoderemre
import copy
import csv
import threading
import yeniMotor
import ultra

def CounterClockwise(ccw,cap,pointCld,RobotLoc,ObjMtx,oldXY):
      
    if ccw==2:
        count=6
        return count,pointCld,RobotLoc,ObjMtx,oldXY
    
    if ccw==3:
        count=6
        return count,pointCld,RobotLoc,ObjMtx,oldXY
        
    if ccw==4:
	
        count=4
            
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.1)
                        
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
            

        count=5
        time.sleep(0.01)
            
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        

        count=6
        time.sleep(0.01)
        
        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY        
		
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        count=7
		
        if(ultra.distance(-1)<20):            
            return count,pointCld,RobotLoc,ObjMtx,oldXY
			
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
		
        count=8
        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY 
			
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        count=1
		
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY 
			
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        count=2
        pointCld,ObjMtx, oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)
        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY 
			
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        count=3
        return count,pointCld,RobotLoc,ObjMtx,oldXY
		      
    if ccw==5:
	    
        count=5
        time.sleep(0.01)
		
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
            
        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        

        count=6
        time.sleep(0.01)
        
        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY        
		
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        count=7
		
        if(ultra.distance(-1)<20):            
            return count,pointCld,RobotLoc,ObjMtx,oldXY
			
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
		
        count=8
        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY 
			
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        count=1
		
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY 
			
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        count=2
        pointCld,ObjMtx, oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)
		
        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY 
			
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        count=3
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY 
		
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        count=4
        pointCld,ObjMtx, oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)
        return count,pointCld,RobotLoc,ObjMtx,oldXY
	
        
    if ccw==6:
        
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        

        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
        
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        count=7    
        

        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
     
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        
        count=8
        time.sleep(0.01)
        #taramayı atlıyor
        

        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
			
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        count=1        
        
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
        
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
            

        count=2
        time.sleep(0.01)
            
        pointCld,ObjMtx, oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)

            

        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        count=3
            
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
            

        count=4
        time.sleep(0.01)
                        
        pointCld,ObjMtx, oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)

            
        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            

        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
            
        count=5
        
        return count,pointCld,RobotLoc,ObjMtx,oldXY#bitiyor           
                
    if ccw==7:
	
        count=7 
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        
        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
     
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        
        count=8
        time.sleep(0.01)
        #taramayı atlıyor
        

        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
			
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        count=1        
        
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
        
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
            

        count=2
        time.sleep(0.01)
            
        pointCld,ObjMtx, oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)

            

        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        count=3
            
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
            

        count=4
        time.sleep(0.01)
                        
        pointCld,ObjMtx, oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)

            
        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            

        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
            
        count=5
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
			
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        count=6
        pointCld,ObjMtx, oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)
		
        return count,pointCld,RobotLoc,ObjMtx,oldXY#bitiyor
        
    if ccw==8:
	
        count=8
        RobotLoc=encoderemre.gtime(RobotLoc,-90,0)
        time.sleep(0.01)
        
        if(ultra.distance(0)<20):
            RobotLoc=encoderemre.gtime(RobotLoc,90,0)
            time.sleep(0.01)
            return count,pointCld,RobotLoc,ObjMtx,oldXY
        
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        count=1
        time.sleep(0.01)
         
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
         
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
            

        count=2
        time.sleep(0.01)
            
        pointCld,ObjMtx, oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)

            
        if(ultra.distance(0)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
            

        count=3
            
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
            

        count=4
        time.sleep(0.01)
            
        RobotLoc=encoderemre.gtime(RobotLoc,-90,0)
        time.sleep(0.1)
            
        pointCld,ObjMtx, oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)
 
            
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
            

        count=5
        time.sleep(0.01)
            
        if(ultra.distance(-1)<20):
            return count,pointCld,RobotLoc,ObjMtx,oldXY
            
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        

        count=6
        time.sleep(0.01)
            
        RobotLoc=encoderemre.gtime(RobotLoc,-180,0)
        time.sleep(0.1)
        
        pointCld,ObjMtx, oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)

            
        RobotLoc=encoderemre.gtime(RobotLoc,-180,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        count=7
                    
        return count,pointCld,RobotLoc,ObjMtx,oldXY
    else:
        print('unexpected error')
