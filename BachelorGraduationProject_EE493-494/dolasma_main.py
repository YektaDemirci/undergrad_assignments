import time
import encoderemre
import copy
import csv
import threading
import dolasma_cw
import dolasma_switch_cw
import dolasma_ccw
import dolasma_switch_ccw


def scanObj(pointCld,RobotLoc,ObjMtx,oldXY):
    cap=20
    count,pointCld,RobotLoc,ObjMtx,oldXY=dolasma_cw.Clockwise(cap,pointCld,RobotLoc,ObjMtx,oldXY)  #ilk taramayla birlikte saat yönü dönmeye başla
    casecount=count    
    
    if(count!=6):                                    
    
        while(6!=casecount):                        
            ccw,casecount,pointCld,RobotLoc,ObjMtx,oldXY=dolasma_switch_cw.switchclockwise(casecount,cap,pointCld,RobotLoc,ObjMtx,oldXY)
            
        if(ccw==2):#cw'da 6ya denk geliyor
            return pointCld,RobotLoc,ObjMtx,oldXY
        
        else:
            count,pointCld,RobotLoc,ObjMtx,oldXY=dolasma_ccw.CounterClockwise(ccw,cap,pointCld,RobotLoc,ObjMtx,oldXY)
            ccwcasecount=count
            
            while(6!=ccwcasecount):
                ccwcasecount,pointCld,RobotLoc,ObjMtx,oldXY=dolasma_switch_ccw.switchcounterclockwise(ccwcasecount,cap,pointCld,RobotLoc,ObjMtx,oldXY)
    		
        return pointCld,RobotLoc,ObjMtx,oldXY
        
    return pointCld,RobotLoc,ObjMtx,oldXY 


            
 

     



    
       
