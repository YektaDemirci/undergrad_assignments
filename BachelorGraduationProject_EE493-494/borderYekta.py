# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:49:05 2019

@author: Yekta
"""
import cv2
import csv
import numpy as np
import copy
import matplotlib
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import math
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

pointCld = list(csv.reader(open("./kare2.csv")))



xMain=[]
yMain=[]
for i in pointCld:
    xMain.append(float(i[0]))
    yMain.append(float(i[1]))

overallMap=np.asarray(pointCld)

#    plt.scatter(robotLoc[0],robotLoc[1],s=1,c='y')
#    plt.scatter(xMain,yMain,s=1,c='b',dpi=300)
#xM = list(csv.reader(open("xFiltered.csv")))
#yM = list(csv.reader(open("yFiltered.csv")))
#
#xMain=list(map(int, [j for sub in xM for j in sub]))
#yMain=list(map(int, [j for sub in yM for j in sub]))

minX=min(xMain)
maxX=max(xMain)
minY=min(yMain)
maxY=max(yMain)

xFin=copy.deepcopy(xMain)
yFin=copy.deepcopy(yMain)

xFin[:] = [round(x - minX) for x in xMain]
yFin[:] = [round(y - minY) for y in yMain]

#margin must be even

margin=100
hmargin=int(margin/2)
dotLen=5
dot2=50

shift=10

#    overallMap=[]
#    for indo in range(0,len(xFin)):
#        overallMap.append([xFin[indo]+hmargin,yFin[indo]+hmargin])
#    overallMap=np.asarray(pointCld)


kalanX = ( (max(yFin)+margin ) % shift )
kalanY = ( (max(xFin)+margin ) % shift ) 

kalanY, kalanX, xFin, yFin = int(kalanY), int(kalanX), [int(element) for element in xFin], [int(element) for element in yFin]


#shape = (int(max(yFin)+margin+kalanY), int(max(xFin)+margin+kalanX))
 
toDel = np.ones((max(yFin)+margin+kalanY,max(xFin)+margin+kalanX),np.uint8)*255
dummyMap = np.ones((max(yFin)+margin+kalanY,max(xFin)+margin+kalanX),np.uint8)*255
edgs = np.ones((max(yFin)+margin+kalanY,max(xFin)+margin+kalanX),np.uint8)*255

#toDel = np.ones(shape, np.uint8)*255
#dummyMap = np.ones(shape, np.uint8)*255
#edgs = np.ones(shape, np.uint8)*255


for index in range(0,len(xFin)):
    dummyMap[(yFin[index]+hmargin)-dotLen:(yFin[index]+hmargin)+dotLen,(xFin[index]+hmargin)-dotLen:(xFin[index]+hmargin)+dotLen]=1
    toDel[(yFin[index]+hmargin),(xFin[index]+hmargin)]=1


#img = cv2.imread("new.png")
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(dummyMap, 75, 100)
#plt.imshow(edges)


#cv2.HoughLinesP(image,rho, theta, threshold, np.array ([ ]), minLineLength=xx, maxLineGap=xx)
lines = cv2.HoughLinesP(edges, 1, np.pi/36, 60, maxLineGap=300)
 


for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(edgs, (x1, y1), (x2, y2), 1, 5)
    
#plt.imshow(edgs)

ra=np.where(edgs==1)

xAft=ra[0][:].tolist()
yAft=ra[1][:].tolist()
#plt.scatter(xAft,yAft)

for indx in range(0,len(xAft)):
    toDel[xAft[indx]-dot2:xAft[indx]+dot2,yAft[indx]-dot2:yAft[indx]+dot2]=255

za=np.where(toDel==1)

xObj=za[1][:].tolist()
yObj=za[0][:].tolist()
#    plt.scatter(xObj,yObj,s=1)

cisimler=[]
duvarlarX=[]
duvarlarY=[]

for o in range(0,len(xAft)):
    duvarlarX.append(yAft[o]+minX-hmargin)
    duvarlarY.append(xAft[o]+minY-hmargin)

for a in range(0,len(xObj)):
    cisimler.append([xObj[a]+minX-hmargin,yObj[a]+minY-hmargin])
    
cisimler=np.asarray(cisimler)

'''Fazla cisim icin elbow method koy'''

kmeans = KMeans(n_clusters=1 ).fit(cisimler)
centers=kmeans.cluster_centers_
centers=np.round(centers)

ine=kmeans.inertia_
#
#    
#    fig = plt.figure()#frameon=False)
#    plt.axis('off')
#    ax1 = fig.add_subplot(111)
#    ax1.scatter(duvarlarX,duvarlarY ,s=1,c='green')
#    ax1.scatter(cisimler[:,0],cisimler[:,1] ,s=1,c='blue')
#    ax1.scatter(centers[:,0],centers[:,1] ,s=10,c='red')
#    fig.savefig('zakkum.jpeg', dpi=300)
##    plt.show()
#    plt.close()

ra=kmeans.labels_
    
dist1=[]
#dist2=[]

for index in range(0,len(ra)):
#    if ra[index] == 0:
    dist1.append(math.sqrt((cisimler[index,0]-centers[0,0])**2+(cisimler[index,1]-centers[0,1])**2))
#    elif ra[index] == 1:
#        dist2.append(math.sqrt((mean[index,0]-centers[1,0])**2+(mean[index,1]-centers[1,1])**2))
        
        
# 
disto=sum(dist1)/len(dist1)


if disto <= 28:
    
    fig, ax = plt.subplots()#frameon=False)
    plt.axis('off')
    ax1 = fig.add_subplot(111)
    ax1.scatter(duvarlarX,duvarlarY ,s=1,c='green')
    circle1 = plt.Circle((centers[0,0], centers[0,1]), 25, color='b', fill=False)       
    ax1.add_artist(circle1)
#        ax1.scatter(cisimler[:,0],cisimler[:,1] ,s=1,c='blue')
    ax1.scatter(centers[0,0],centers[0,1] ,s=10,c='red')
    fig.savefig('zakkum.jpeg', dpi=300)
    #    plt.show()
    plt.close()
    
    img = Image.open('zakkum.jpeg')
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("arial.ttf", 50)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0,0 ,0),"This is small circle, coordinates of the centre are x="+str(centers[0,0])+" , y="+str(centers[0,1]), (0,0,0),font=font)
    img.save('fin_img.jpg')
    
elif ( (28 < disto) and (disto<=36) ):
    
    fig, ax = plt.subplots()#frameon=False)
    plt.axis('off')
    ax1 = fig.add_subplot(111)
    ax1.scatter(duvarlarX,duvarlarY ,s=1,c='green')
    points=[[centers[0,0]-40,centers[0,1]-23.1],[centers[0,0],centers[0,1]+46.2],[centers[0,0]+40,centers[0,1]-23.1]]
    circle1 = plt.Polygon(points,color='b', fill=False)   
    ax1.add_artist(circle1)
#        ax1.scatter(cisimler[:,0],cisimler[:,1] ,s=1,c='blue')
    ax1.scatter(centers[0,0],centers[0,1] ,s=10,c='red')
    fig.savefig('zakkum.jpeg', dpi=300)
    #    plt.show()
    plt.close()
    
    
    img = Image.open('zakkum.jpeg')
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("arial.ttf", 50)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0,0 ,0),"This is triangle, coordinates of the centre are x="+str(centers[0,0])+" , y="+str(centers[0,1]), (0,0,0),font=font)
    img.save('fin_img.jpg')
    
    
elif ( (36 < disto) and (disto<=44) ):
    
    fig, ax = plt.subplots()#frameon=False)
    plt.axis('off')
    ax1 = fig.add_subplot(111)
    ax1.scatter(duvarlarX,duvarlarY ,s=1,c='green')
    circle1 = plt.Rectangle((centers[0,0]-35, centers[0,1]-35), 70, 70, angle=0,color='b', fill=False)       
    ax1.add_artist(circle1)
#        ax1.scatter(cisimler[:,0],cisimler[:,1] ,s=1,c='blue')
    ax1.scatter(centers[0,0],centers[0,1] ,s=10,c='red')
    fig.savefig('zakkum.jpeg', dpi=300)
    #    plt.show()
    plt.close()
    
    
    img = Image.open('zakkum.jpeg')
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("arial.ttf", 50)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0,0 ,0),"This is square, coordinates of the centre are x="+str(centers[0,0])+" , y="+str(centers[0,1]), (0,0,0),font=font)
    img.save('fin_img.jpg')
    
    
    
elif (44 < disto) :
    
    fig, ax = plt.subplots()#frameon=False)
    plt.axis('off')
    ax1 = fig.add_subplot(111)
    ax1.scatter(duvarlarX,duvarlarY ,s=1,c='green')
    circle1 = plt.Circle((centers[0,0], centers[0,1]), 50, color='b', fill=False)       
    ax1.add_artist(circle1)
#        ax1.scatter(cisimler[:,0],cisimler[:,1] ,s=1,c='blue')
    ax1.scatter(centers[0,0],centers[0,1] ,s=10,c='red')
    fig.savefig('zakkum.jpeg', dpi=300)
    #    plt.show()
    plt.close()
    
    
    
    img = Image.open('zakkum.jpeg')
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("DejaVuSerif.ttf", 50)
    # draw.text((x, y),"Sample Text",(r,g,b))
    #draw.text((0, 0), "asdasdasdsa", (0, 0, 0))
    draw.text((0, 0),"This is big circle, coordinates of the centre are x="+str(centers[0,0])+" , y="+str(centers[0,1]), (0,0,0),font=font)
    img.save('fin_img.jpg')
    #img.show()

print('Map is ready')
    
