import math
import copy

def didIsee(oldObjMtx,newObjMtx):
    retMtx=[]
    oold=copy.deepcopy(oldObjMtx)
    neew=copy.deepcopy(newObjMtx)
    
    if (len(oldObjMtx)==0):
        retMtx=newObjMtx
        return retMtx
    elif (len(newObjMtx)==0):
        retMtx=oldObjMtx
        return retMtx
    else:
        for x in neew:
        #    seen=0
            flag = 0
            for k in oold:
                dist=math.sqrt(((x[0]-k[0])**2)+((x[1]-k[1])**2))
                if(dist<=150):
                 #   k[2]=k[2]+1
                 #   k[0]=(k[2]*k[0]+x[0])/(k[2])
                 #   k[1]=(k[1]*k[2]+x[1])/(k[2])
                    retMtx.append(k)
                    flag =1
                    break
                else:
                    continue
            if(flag ==0):
                retMtx.append(x)
            
        for x in oold:
        #    seen=0
            flag=0
            for k in retMtx:
                dist=math.sqrt(((x[0]-k[0])**2)+((x[1]-k[1])**2))
                print('dist=',dist)
                if(dist<=150):
                    flag=1
                    break
                else:
                    continue
    
            if(flag ==0):
                retMtx.append(x)
         
                        
        return retMtx
