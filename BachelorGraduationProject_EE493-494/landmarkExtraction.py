import matplotlib
from matplotlib import pyplot as plt
import copy
import math
import did_I_see
def landmarkExtraction(robotLoc,pointCld,oldObjMtx):

  #  import polar2cart
    prevMin=0
    print(pointCld)

    diff=[]
    objMtx=[] # [rot,dist]

#    pointCld=polar2cart.relativePolar(robotLoc,pointCld) # robotun konumu da al,matris de al
    
    #sortedData = sorted(pointCld, key=lambda x: x[1])
    
    for x in range(len(pointCld)-1):
        diff.append((math.sqrt(((robotLoc[0]-pointCld[x+1][0])**2)+((robotLoc[1]-pointCld[x+1][1])**2)))-(math.sqrt(((robotLoc[0]-pointCld[x][0])**2)+((robotLoc[1]-pointCld[x][1])**2))))

    distance=[]
    for k in pointCld:
        distance.append((math.sqrt(((robotLoc[0]-k[0])**2)+((robotLoc[1]-k[1])**2))))
    winLngth=30

    halfdiff=diff
    halfdiff=halfdiff[(len(halfdiff)-40):len(halfdiff)]+halfdiff
    #plt.plot(diff)
    #plt.show(block=True)
    #######inş iyi extraction
    while(True):
  
        objMinIdx, objMin=halfdiff.index(min(halfdiff)), min(halfdiff)


        if(abs(objMin)<90 or objMin==prevMin):
            print('objMtx=,oldMtx',objMtx,oldObjMtx)
            if(len(objMtx)==0):
                return oldObjMtx
                
            objMtx=copy.deepcopy(did_I_see.didIsee(oldObjMtx,objMtx))
            ########## buraya did_I_see gelsin
            if (len(objMtx)==0):
                return oldObjMtx
            else:
                return objMtx
            
            break
      

        win=halfdiff[objMinIdx:objMinIdx+winLngth]
        objMaxIdx, objMax=win.index(max(win))+objMinIdx, max(win)
        windowedData=distance[objMinIdx:objMaxIdx]
        print(objMaxIdx,objMinIdx)
 #       objasilLoc=objMinIdx+pointCld[objMinIdx:objMaxIdx].index(min(pointCld[objMinIdx:objMaxIdx]))
        objIndex=objMinIdx+windowedData.index(min(windowedData))
        objasilLoc=pointCld[objIndex-41]
        print(objasilLoc, min(pointCld[objMinIdx:objMaxIdx]))
        centerScale=(distance[objIndex-41]+50)/(distance[objIndex-41])
        if(objMax>50):  ## değerler max min testlerine göre değişecek
            objLoc=objasilLoc
#            objX=-1*float(pointCld[round(objLoc)])*math.sin(0.01*math.pi*objLoc)
#            objY=float(pointCld[round(objLoc)])*math.cos(0.01*math.pi*objLoc)
            
            xLoc = robotLoc[0]+((objLoc[0]-robotLoc[0])*centerScale)
            yLoc = robotLoc[1]+((objLoc[1]-robotLoc[1])*centerScale)
                    
                
            objMtx.append([xLoc,yLoc,0])
            halfdiff[int(objMinIdx-(objIndex-objMinIdx)):int(objMaxIdx+objIndex-objMinIdx)]=[1]*len( halfdiff[int(objMinIdx-(objIndex-objMinIdx)):int(objMaxIdx+objIndex-objMinIdx)]) ## objenin olduğu yerleri sıfırla / final kısımda sıkıntı çıkmaması için ayar çek
            print(objMtx)
        prevMin=objMin
