# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:35:39 2019
@author: Yekta
"""
import matplotlib
from matplotlib import pyplot as plt
import numpy as  np
import copy
import csv
import math

#plt.scatter(xMain,yMain,s=1)


#xM = list(csv.reader(open("xFiltered.csv")))
#yM = list(csv.reader(open("yFiltered.csv")))

#xMain=list(map(int, [j for sub in xM for j in sub]))
#yMain=list(map(int, [j for sub in yM for j in sub]))


'Current location '
#curX=400
#curY=600

#xMain.append(950)
#yMain.append(900)


'Destination location'
#xMain.append(400)
#yMain.append(350)

#desX=1000
#desY=600



def reverse(tempoX,tempoY,patho):
    sonEleman=patho[-1]
    if sonEleman==4:
        tempoX=tempoX
        tempoY=tempoY-1
    elif sonEleman==2:
        tempoX=tempoX
        tempoY=tempoY+1
    elif sonEleman==3:
        tempoX=tempoX+1
        tempoY=tempoY
    elif sonEleman==1:
        tempoX=tempoX-1
        tempoY=tempoY
    del patho[-1]
    
    return(tempoX,tempoY,patho)
    

def pathArray(sonYol,window,currX,currY):
    
    indx=0
    finYol=[[]]
    finYol[indx].append(sonYol[0])
    

    
    for i in range(1,len(sonYol)):
        if finYol[indx][-1] == sonYol[i]:
            finYol[indx].append(sonYol[i])
        else:
            finYol.append([])
            indx=indx+1
            finYol[indx].append(sonYol[i])
    
    ultraFin=[]
    
    for i in finYol:
        uzunluk=len(i)
        if i[0]==1:
            currX=currX+uzunluk*window
            currY=currY
            
            ultraFin.append([currX,currY])
            
        elif i[0]==3:
            
            currX=currX-uzunluk*window
            currY=currY
            
            ultraFin.append([currX,currY])

        elif i[0]==2:
            currY=currY-uzunluk*window
            currX=currX
            
            ultraFin.append([currX,currY])
            
        if i[0]==4:
            currY=currY+uzunluk*window
            currX=currX
            ultraFin.append([currX,currY])
        else:
            continue
        
    return ultraFin
                    
    

def runForest(pointCld,robotLoc,destination):
    xMain=[]
    yMain=[]
    curX=robotLoc[0]
    curY=robotLoc[1]
    
    desX=destination[0]
    desY=destination[1]
    
    uzaklik=math.sqrt(((curX-desX)**2)+((curY-desY)**2))
    scale=(uzaklik-260)/uzaklik
    
    desX=curX+((desX-curX)*scale)
    desY=curY+((desY-curY)*scale)
    
    for x in pointCld:
        xMain.append(x[0])
            
    for x in pointCld:
        yMain.append(x[1])

    minX=min(xMain)
    maxX=max(xMain)
    minY=min(yMain)
    maxY=max(yMain)
    
    xFin=copy.deepcopy(xMain)
    yFin=copy.deepcopy(yMain)
    
    xFin[:] = [round(x - minX) for x in xMain]
    yFin[:] = [round(y - minY) for y in yMain]
    
    curX = round(curX-minX)
    desX = round(desX-minX)
    
    curY = round(curY-minY)
    desY = round(desY-minY)
    
    #margin must be even
    
    margin=120
    hmargin=int(margin/2)
    dotLen=50
    
    curX=curX+hmargin
    desX=desX+hmargin
    curY=curY+hmargin
    desY=desY+hmargin
    
    shift=5
    
    kalanX = ( (max(yFin)+margin ) % shift )
    kalanY = ( (max(xFin)+margin ) % shift ) 
    
    dummyMap = np.zeros((max(yFin)+margin+kalanY,max(xFin)+margin+kalanX),np.bool)
    
    for index in range(0,len(xFin)):
        dummyMap[(yFin[index]+hmargin)-dotLen:(yFin[index]+hmargin)+dotLen,(xFin[index]+hmargin)-dotLen:(xFin[index]+hmargin)+dotLen]=1
    
    lowMap=[]
    
    curIndx=[int(curY/shift)-1,int(curX/shift)]
    destIndx=[int(desY/shift)-1,int(desX/shift)]
    
    for yWin in range(0,np.size(dummyMap,0),shift):
        aRow=[]
        for xWin in range(0,np.size(dummyMap,1),shift):
            search=dummyMap[yWin:yWin+shift,xWin:xWin+shift]
            
            if np.count_nonzero(search)  > 0:
                aRow.append(1)
            else:
                aRow.append(0)
            
        lowMap.append(aRow)
    
    tempY=curIndx[0]
    tempX=curIndx[1]
    
#    plt.imshow(lowMap)
    
    
    '2 means go up, 1 means go right, 3 means go left, 4 means go down'
    paths=[]
    paths.append([])
    
    pathIndx=0
    
    paths[pathIndx].append(10)
    
    paths.append(copy.deepcopy(paths[pathIndx]))
    pathIndx=pathIndx+1
    
    paths[pathIndx].append(20)
    
    'If control 0 then increase Y direction, elseif 1 then increase X'
    control1=0
    
    while (tempY != destIndx[0]) or (tempX != destIndx[1]):
#        print(tempY,tempX)
 #       time.sleep(0.5)
        farkY=destIndx[0]-tempY
        farkX=destIndx[1]-tempX
        
        if control1==0:
            
            if farkY < 0:
                
                if lowMap[tempY-1][tempX] == 0:
                    
                    if paths[pathIndx][-1]==4:
                        if(lowMap[tempY+1][tempX]==0):
                          #  lowMap[tempY][tempX]=1
                            tempY=tempY+1
                            tempX=tempX
                            farkY=destIndx[0]-tempY
                            farkX=destIndx[1]-tempX
                            paths[pathIndx].append(4)
                            control1=0
                        elif (lowMap[tempY+1][tempX]==1):
                            lowMap[tempY][tempX]=1
                            [tempX,tempY,paths[pathIndx]] = reverse(tempX,tempY,paths[pathIndx])
                            control1=1 #
                    else:
                        paths[pathIndx].append(2)
                        tempY=tempY-1
                        tempX=tempX
    
                    
                else:
                    if paths[pathIndx]==paths[pathIndx-1]:
                        if (lowMap[tempY][tempX+1]==1) and (lowMap[tempY][tempX-1]==1):
                            lowMap[tempY][tempX]=1
                            'son eleman sil kodu yaz'
                            [tempX,tempY,paths[pathIndx]] = reverse(tempX,tempY,paths[pathIndx])
                            control1=1#
                            
                        else:
                        
                            if(lowMap[tempY][tempX+1]==0 and farkX>=0):
                           #     lowMap[tempY][tempX]=1
                                tempY=tempY
                                tempX=tempX+1
                                farkY=destIndx[0]-tempY
                                farkX=destIndx[1]-tempX
                                
                                if paths[pathIndx][-1]==4:
                                    paths[pathIndx].append(4)
                                    
                                if paths[pathIndx][-1]==2:
                                    paths[pathIndx].append(2)
                                    
                                else:
                                    paths[pathIndx].append(1)

                                control1=1#
                                
                            elif(lowMap[tempY][tempX-1]==0):
                          #      lowMap[tempY][tempX]=1
                                tempY=tempY
                                tempX=tempX-1
                                farkY=destIndx[0]-tempY
                                farkX=destIndx[1]-tempX
                                if paths[pathIndx][-1]==4:
                                    paths[pathIndx].append(4)
                                    
                                if paths[pathIndx][-1]==2:
                                    paths[pathIndx].append(2)
                                    
                                else:
                                    paths[pathIndx].append(3)
                                control1=1
                    else:
                        paths.append(copy.deepcopy(paths[pathIndx]))
                        pathIndx=pathIndx+1
                        control1=1
                        
            elif farkY > 0:
                
                if lowMap[tempY+1][tempX] == 0:
                    if paths[pathIndx][-1]==2:
                        if(lowMap[tempY-1][tempX]==0):
                        #    lowMap[tempY][tempX]=1
                            tempY=tempY-1
                            tempX=tempX
                            farkY=destIndx[0]-tempY
                            farkX=destIndx[1]-tempX
                            paths[pathIndx].append(2)
                            control1=0
                        elif (lowMap[tempY-1][tempX]==1):
                            lowMap[tempY][tempX]=1
                            [tempX,tempY,paths[pathIndx]] = reverse(tempX,tempY,paths[pathIndx])
                            control1=1#
                    else:
                        tempY=tempY+1
                        tempX=tempX
                        farkY=destIndx[0]-tempY
                        farkX=destIndx[1]-tempX
                        paths[pathIndx].append(4)
                    
                else:
                    if paths[pathIndx]==paths[pathIndx-1]:
                        if (lowMap[tempY][tempX+1]==1) and (lowMap[tempY][tempX-1]==1):
                            lowMap[tempY][tempX]=1
                            [tempX,tempY,paths[pathIndx]] = reverse(tempX,tempY,paths[pathIndx])
                            control1=1#
                            
                        else:
                            if(lowMap[tempY][tempX+1]==0 and farkX>=0):
                       #         lowMap[tempY][tempX]=1
                                tempY=tempY
                                tempX=tempX+1
                                farkY=destIndx[0]-tempY
                                farkX=destIndx[1]-tempX
                                if paths[pathIndx][-1]==4:
                                    paths[pathIndx].append(4)
                                    
                                if paths[pathIndx][-1]==2:
                                    paths[pathIndx].append(2)
                                    
                                else:
                                    paths[pathIndx].append(1)
                                control1=1
                                
                            elif(lowMap[tempY][tempX-1]==0):
                          #      lowMap[tempY][tempX]=1
                                tempY=tempY
                                tempX=tempX-1
                                farkY=destIndx[0]-tempY
                                farkX=destIndx[1]-tempX
                                if paths[pathIndx][-1]==4:
                                    paths[pathIndx].append(4)
                                    
                                if paths[pathIndx][-1]==2:
                                    paths[pathIndx].append(2)
                                    
                                else:
                                    paths[pathIndx].append(3)
                                control1=1
                    else:
                        paths.append(copy.deepcopy(paths[pathIndx]))
                        pathIndx=pathIndx+1
                        control1=1
                        
            elif farkY == 0:
                control1=1
                        
        if control1==1:
            
            if farkX < 0:
                
                if lowMap[tempY][tempX-1] == 0:
                    
                    if paths[pathIndx][-1]==1:
                        if(lowMap[tempY][tempX+1]==0):
                       #     lowMap[tempY][tempX]=1
                            tempY=tempY
                            tempX=tempX+1
                            farkY=destIndx[0]-tempY
                            farkX=destIndx[1]-tempX
                            paths[pathIndx].append(1)
                            control1=1
                        elif (lowMap[tempY][tempX+1]==1):
                            lowMap[tempY][tempX]=1
                            [tempX,tempY,paths[pathIndx]] = reverse(tempX,tempY,paths[pathIndx])
                            control1=0#
                    else:
                        tempY=tempY
                        tempX=tempX-1
                        farkY=destIndx[0]-tempY
                        farkX=destIndx[1]-tempX
                        paths[pathIndx].append(3)
                    
                    
                else:
                    if paths[pathIndx]==paths[pathIndx-1]:
                        if (lowMap[tempY+1][tempX]==1) and (lowMap[tempY-1][tempX]==1):
                            lowMap[tempY][tempX]=1
                            [tempX,tempY,paths[pathIndx]] = reverse(tempX,tempY,paths[pathIndx])
                            control1=0#
                            
                        else:
#########                            
                            if(lowMap[tempY+1][tempX]==0 and farkY>=0):
                          #      lowMap[tempY][tempX]=1
                                tempY=tempY+1
                                tempX=tempX
                                farkY=destIndx[0]-tempY
                                farkX=destIndx[1]-tempX
                                if paths[pathIndx][-1]==1:
                                    paths[pathIndx].append(1)
                                    
                                if paths[pathIndx][-1]==3:
                                    paths[pathIndx].append(3)
                                    
                                else:
                                    paths[pathIndx].append(4)
                                control1=0
                            elif(lowMap[tempY-1][tempX]==0):
                           #     lowMap[tempY][tempX]=1
                                tempY=tempY-1
                                tempX=tempX
                                farkY=destIndx[0]-tempY
                                farkX=destIndx[1]-tempX
                                
                                if paths[pathIndx][-1]==1:
                                    paths[pathIndx].append(1)
                                    
                                if paths[pathIndx][-1]==3:
                                    paths[pathIndx].append(3)
                                    
                                else:
                                    paths[pathIndx].append(2)

                                control1=0
                                
                    else:
                        paths.append(copy.deepcopy(paths[pathIndx]))
                        pathIndx=pathIndx+1
                        control1=0
            
            elif farkX > 0:
                
                if lowMap[tempY][tempX+1] == 0:
                    if paths[pathIndx][-1]==3:
                        if(lowMap[tempY][tempX-1]==0):
                          #  lowMap[tempY][tempX]=1
                            tempY=tempY
                            tempX=tempX-1
                            farkY=destIndx[0]-tempY
                            farkX=destIndx[1]-tempX
                            paths[pathIndx].append(3)
                            control1=1
                        elif (lowMap[tempY][tempX-1]==1):
                            lowMap[tempY][tempX]=1
                            [tempX,tempY,paths[pathIndx]] = reverse(tempX,tempY,paths[pathIndx])
                            control1=0
                    else:
                        tempY=tempY
                        tempX=tempX+1
                        farkY=destIndx[0]-tempY
                        farkX=destIndx[1]-tempX
                        paths[pathIndx].append(1)
                    
                else:
                    if paths[pathIndx]==paths[pathIndx-1]:
                        if (lowMap[tempY+1][tempX]==1) and (lowMap[tempY-1][tempX]==1):
                            lowMap[tempY][tempX]=1
                            [tempX,tempY,paths[pathIndx]] = reverse(tempX,tempY,paths[pathIndx])
                            control1=1#
                            
                        else:
                            
                            if(lowMap[tempY+1][tempX]==0 and farkY>=0):
                           #     lowMap[tempY][tempX]=1
                                tempY=tempY+1
                                tempX=tempX
                                farkY=destIndx[0]-tempY
                                farkX=destIndx[1]-tempX
                                
                                if paths[pathIndx][-1]==1:
                                    paths[pathIndx].append(1)
                                    
                                if paths[pathIndx][-1]==3:
                                    paths[pathIndx].append(3)
                                    
                                else:
                                    paths[pathIndx].append(4)
                                control1=0
                                
                            elif(lowMap[tempY-1][tempX]==0):
                            #    lowMap[tempY][tempX]=1
                                tempY=tempY-1
                                tempX=tempX
                                farkY=destIndx[0]-tempY
                                farkX=destIndx[1]-tempX
                                
                                if paths[pathIndx][-1]==1:
                                    paths[pathIndx].append(1)
                                    
                                if paths[pathIndx][-1]==3:
                                    paths[pathIndx].append(3)
                                    
                                else:
                                    paths[pathIndx].append(2)

                                control1=0 
                                
                    else:
                        paths.append(copy.deepcopy(paths[pathIndx]))
                        pathIndx=pathIndx+1
                        control1=0
            
            elif farkX == 0:
                control1=0
    
    sonYol=paths[pathIndx]
    
    totalFin=pathArray(sonYol,shift,curX,curY)
    
    for indo in range(0,len(totalFin)):
        totalFin[indo][0]=totalFin[indo][0]+minX-hmargin
        totalFin[indo][1]=totalFin[indo][1]+minY-hmargin
#    print(totalFin)
    #son yolu işleyip return
#    plt.imshow(lowMap)
    return(totalFin)
    
#xler=[]
#yler=[]
#for k in totalFin:
#    xler.append(k[0])
#    yler.append(k[1])
        
#with open("C:/Users/Yekta/Desktop/BitirmeVol2/testMap.csv", 'w', newline='') as myfile:
#    wr = csv.writer(myfile)
#    wr.writerows(lowMap) 
