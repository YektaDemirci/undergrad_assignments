import time
import encoderemre
import copy
import csv
import threading
import yeniMotor
import ultra

def switchcounterclockwise(case,cap,pointCld,RobotLoc,ObjMtx,oldXY):
	

    
    if case==8:
        ccwcasecount=6
        return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
    
    if case==1:
        
        pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)

		
        if(ultra.distance(0)<20):
            ccwcasecount=6
            return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
        
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)


        ccwcasecount=1
        time.sleep(0.01)
        
        if(ultra.distance(-1)<20):
            return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
        
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)

        ccwcasecount=2
        time.sleep(0.01)

        pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)

        
        if(ultra.distance(0)<20):
            return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
        
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        

        ccwcasecount=3
    
        if(ultra.distance(-1)<20):
            return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
        
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.1)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.1)


        ccwcasecount=4
        time.sleep(0.01)

        pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)

        
        if(ultra.distance(0)<20):
            return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
        
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)


        ccwcasecount=5
        time.sleep(0.01)
        
        if(ultra.distance(-1)<20):
            return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
        
        RobotLoc=encoderemre.gtime(RobotLoc,90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)
        

        ccwcasecount=6
        time.sleep(0.01)
    
        pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)       
        return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
        
    if case==2:
        ccwcasecount=6
        return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
    
    if case==3:
        pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)

        if(ultra.distance(0)<20):
            ccwcasecount=6
            return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
        else:
            RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
            time.sleep(0.01)

            ccwcasecount=3
            if(ultra.distance(-1)<20):
                return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
            else:
                RobotLoc=encoderemre.gtime(RobotLoc,90,0)
                time.sleep(0.1)
                RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
                time.sleep(0.1)


                ccwcasecount=4
                time.sleep(0.01)
                
                RobotLoc=encoderemre.gtime(RobotLoc,90,0)
                time.sleep(0.1)

                pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
                time.sleep(0.01)

                
                if(ultra.distance(-1)<20):
                    return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
                
                RobotLoc=encoderemre.gtime(RobotLoc,90,0)
                time.sleep(0.01)
                RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
                time.sleep(0.01)


                ccwcasecount=5
                time.sleep(0.01)
                
                if(ultra.distance(-1)<20):
                    return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
   
                RobotLoc=encoderemre.gtime(RobotLoc,90,0)
                time.sleep(0.01)
                RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
                time.sleep(0.01)


                ccwcasecount=6
                time.sleep(0.01)
       
                RobotLoc=encoderemre.gtime(RobotLoc,-180,0)
                time.sleep(0.1)
        
                pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
                time.sleep(0.01)

            
                return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
    if case==4:
        ccwcasecount=6
        return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
    
    
    if case == 5:

        pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)


        if(ultra.distance(-1)<20):
            ccwcasecount=6
            return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
        else:
            RobotLoc=encoderemre.gtime(RobotLoc,-90,0)
            time.sleep(0.01)
            RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
            time.sleep(0.01)
            ccwcasecount=5
            time.sleep(0.01)

            if(ultra.distance(-1)<20):
                ccwcasecount=5
                return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
            else:
                RobotLoc=encoderemre.gtime(RobotLoc,-90,0)
                time.sleep(0.01)
                if(ultra.distance(0)<20):
                    ccwcasecount=6
                    return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY
                else:
                    RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
                    time.sleep(0.01)

                    ccwcasecount=6
                    time.sleep(0.01)
       
                    RobotLoc=encoderemre.gtime(RobotLoc,-180,0)
                    time.sleep(0.1)

                    pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
                    time.sleep(0.01)

                    return ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY       
                    
