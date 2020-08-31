import time
import encoderemre
import copy
import csv
import threading
import yeniMotor
import ultra


def switchclockwise(case,cap,pointCld,RobotLoc,ObjMtx,oldXY):  #önüne engel çıktığında bir önceki hareketinden başlayarak devam etmeye çalışıyor,eski ölçüm aldığı yerler karşılaştırılıp ölçüm alınmayacak ama burda da kafalar biraz karıştı
      
    if case == 0:
        casecount=6
        ccw=8
        return ccw,casecount,pointCld,RobotLoc,ObjMtx,oldXY

    if case == 1:
        
        pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)

		
        if(ultra.distance(0)<20):
            casecount=6
            ccw=7
            return ccw,casecount,pointCld,RobotLoc,ObjMtx,oldXY

        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)

        casecount=1
        ccw=7
        time.sleep(0.01)

        if(ultra.distance(1)<20):
            return ccw,casecount,pointCld,RobotLoc,ObjMtx,oldXY #gideceği istikameti kontrol ediyor distance checkler hep 90lık dönüşlerden sonra

        RobotLoc=encoderemre.gtime(RobotLoc,-90,0)
        time.sleep(0.01)

        if(ultra.distance(0)<20):
            casecount=6
            return ccw,casecount,pointCld,RobotLoc,ObjMtx,oldXY
  
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)

        casecount=2
        ccw=6
        time.sleep(0.01)

        pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)


        if(ultra.distance(0)<20):
            return ccw,casecount,pointCld,RobotLoc,ObjMtx,oldXY#gideceği istikameti kontrol ediyor distance checkler hep 90lık dönüşlerden sonra

        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.1)

        casecount=3
        ccw=5
    
        if(ultra.distance(1)<20):
            return ccw,casecount,pointCld,RobotLoc,ObjMtx,oldXY

        RobotLoc=encoderemre.gtime(RobotLoc,-90,0)
        time.sleep(0.1)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.1)

        casecount=4
        ccw=4
        time.sleep(0.01)
    
        pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)


    
        if(ultra.distance(1)<20):
            return ccw,casecount,pointCld,RobotLoc,ObjMtx,oldXY
    

        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)

        casecount=5
        ccw=3
        time.sleep(0.01)
    

        if(ultra.distance(1)<20):
            return ccw,casecount,pointCld,RobotLoc,ObjMtx,oldXY
   
        RobotLoc=encoderemre.gtime(RobotLoc,-90,0)
        time.sleep(0.01)
        RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
        time.sleep(0.01)

        casecount=6
        ccw=2
        time.sleep(0.01)

        pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)

            
        return ccw,casecount,pointCld,RobotLoc,ObjMtx,oldXY

    if case == 2:
        casecount=6
        ccw=6
        return ccw,casecount,pointCld,RobotLoc,ObjMtx,oldXY
    
    if case == 3:
        pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)
        ccw=5

        if(ultra.distance(0)<20):
            casecount=6
            return ccw,casecount,pointCld,RobotLoc,ObjMtx, oldXY
        else:
            RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
            time.sleep(0.01)
            casecount=3
            if(ultra.distance(1)<20):
                return ccw,casecount,pointCld,RobotLoc,ObjMtx, oldXY
            else:
                RobotLoc=encoderemre.gtime(RobotLoc,-90,0)
                time.sleep(0.1)
                RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
                time.sleep(0.1)

                casecount=4
                ccw=4
                time.sleep(0.01)

                pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
                time.sleep(0.01)
    
                if(ultra.distance(1)<20):
                    return ccw,casecount,pointCld,RobotLoc,ObjMtx, oldXY

                RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
                time.sleep(0.01)

                casecount=5
                ccw=3
                time.sleep(0.01)
    
    
                if(ultra.distance(1)<20):
                    return ccw,casecount,pointCld,RobotLoc,ObjMtx, oldXY
   
                RobotLoc=encoderemre.gtime(RobotLoc,-90,0)
                time.sleep(0.01)
                RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
                time.sleep(0.01)

                casecount=6
                ccw=2
                time.sleep(0.01)

                pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
                time.sleep(0.01)
           
                return ccw,casecount,pointCld,RobotLoc,ObjMtx, oldXY


    if case == 4:
        
        casecount=6
        ccw=4
        return ccw,casecount,pointCld,RobotLoc,ObjMtx, oldXY

    if case == 5:

        pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
        time.sleep(0.01)
        ccw=3

        if(ultra.distance(1)<20):
            casecount=6
            return ccw,casecount,pointCld,RobotLoc,ObjMtx, oldXY
        else:

            RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
            time.sleep(0.01)
            casecount=5
            time.sleep(0.01)

            if(ultra.distance(1)<20):
                casecount=5
                return ccw,casecount,pointCld,RobotLoc,ObjMtx, oldXY
            else:
                RobotLoc=encoderemre.gtime(RobotLoc,-90,0)
                time.sleep(0.01)
                if(ultra.distance(0)<20):
                    casecount=6
                    return ccw,casecount,pointCld,RobotLoc,ObjMtx, oldXY
                else:
                    RobotLoc=encoderemre.gtime(RobotLoc,0,cap)
                    time.sleep(0.01)

                    casecount=6
                    ccw=2
                    time.sleep(0.01)

                    pointCld,ObjMtx,oldXY=yeniMotor.scan(RobotLoc,pointCld,ObjMtx,oldXY)
                    time.sleep(0.01)

                    return ccw,casecount,pointCld,RobotLoc,ObjMtx, oldXY
        
                
   
       
