import math
def polar2cart(robotLoc,liste):
    cartList=[]
    for k in liste:
        x = k[0]*math.cos(math.radians(k[1])) + robotLoc[0]
        y = k[0]*math.sin(math.radians(k[1])) + robotLoc[1]
        cartList.append([x,y])

    return cartList
    
    
def polar2cart2(robotLoc,liste,aOff):
    cartList=[]
    for k in liste:
        x = k[0]*math.cos(aOff+math.radians(k[1])) + robotLoc[0]
        y = k[0]*math.sin(aOff+math.radians(k[1])) + robotLoc[1]
        cartList.append([x,y])

    return cartList

def relativePolar(robotLoc,cartList):
    polarList=[]
    for k in cartList:
        r = math.sqrt((k[0]-robotLoc[0])**2)+((k[1]-robotLoc[1])**2)
        teta = math.atan2((k[1]-robotLoc[1]),(k[0]-robotLoc[0]))
        teta=math.degrees(teta)-robotLoc[2]
        polarList.append([r,teta])

    return polarList

        




