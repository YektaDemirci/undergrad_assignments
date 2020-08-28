# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 22:31:17 2018

@author: Yekta
"""

import pickle
data = pickle.load(open('/Users/Yekta/Desktop/ODTU2/499/Hw2/car.pkl','rb'))
train = data ['train']
test = data ['test']

un0=ac0=gd0=vgd0=0
un1=ac1=gd1=vgd1=0
un2=ac2=gd2=vgd2=0
un3=ac3=gd3=vgd3=0

for z in range(0,2):
    for i in range(0,1150):
        if train[i][z]=='low':
            if train[i][6]=='unacc':
                un0 += 1
            elif train[i][6]=='acc':
                ac0 += 1
            elif train[i][6]=='good':
                gd0 += 1
            elif train[i][6]=='vgood':
                vgd0 += 1
        elif train[i][z]=='med':
            if train[i][6]=='unacc':
                un1 += 1
            elif train[i][6]=='acc':
                ac1 += 1
            elif train[i][6]=='good':
                gd1 += 1
            elif train[i][6]=='vgood':
                vgd1 += 1
        elif train[i][z]=='high':
            if train[i][6]=='unacc':
                un2 += 1
            elif train[i][6]=='acc':
                ac2 += 1
            elif train[i][6]=='good':
                gd2 += 1
            elif train[i][6]=='vgood':
                vgd2 += 1
        elif train[i][z]=='vhigh':
            if train[i][6]=='unacc':
                un3 += 1
            elif train[i][6]=='acc':
                ac3 += 1
            elif train[i][6]=='good':
                gd3 += 1
            elif train[i][6]=='vgood':
                vgd3 += 1
    if z==0:
        buy=[[vgd0,gd0,ac0,un0],[vgd1,gd1,ac1,un1],[vgd2,gd2,ac2,un2],[vgd3,gd3,ac3,un3]]
        un0=ac0=gd0=vgd0=un1=ac1=gd1=vgd1=un2=ac2=gd2=vgd2=un3=ac3=gd3=vgd3=0
    elif z==1:
        maint=[[vgd0,gd0,ac0,un0],[vgd1,gd1,ac1,un1],[vgd2,gd2,ac2,un2],[vgd3,gd3,ac3,un3]]
        un0=ac0=gd0=vgd0=un1=ac1=gd1=vgd1=un2=ac2=gd2=vgd2=un3=ac3=gd3=vgd3=0
        
for i in range(0,1150):
    if train[i][2]=='5more':
        if train[i][6]=='unacc':
            un0 += 1
        elif train[i][6]=='acc':
            ac0 += 1
        elif train[i][6]=='good':
            gd0 += 1
        elif train[i][6]=='vgood':
            vgd0 += 1
    elif train[i][2]=='4':
        if train[i][6]=='unacc':
            un1 += 1
        elif train[i][6]=='acc':
            ac1 += 1
        elif train[i][6]=='good':
            gd1 += 1
        elif train[i][6]=='vgood':
            vgd1 += 1
    elif train[i][2]=='3':
        if train[i][6]=='unacc':
            un2 += 1
        elif train[i][6]=='acc':
            ac2 += 1
        elif train[i][6]=='good':
            gd2 += 1
        elif train[i][6]=='vgood':
            vgd2 += 1
    elif train[i][2]=='2':
        if train[i][6]=='unacc':
            un3 += 1
        elif train[i][6]=='acc':
            ac3 += 1
        elif train[i][6]=='good':
            gd3 += 1
        elif train[i][6]=='vgood':
            vgd3 += 1
doors=[[vgd0,gd0,ac0,un0],[vgd1,gd1,ac1,un1],[vgd2,gd2,ac2,un2],[vgd3,gd3,ac3,un3]]
un0=ac0=gd0=vgd0=un1=ac1=gd1=vgd1=un2=ac2=gd2=vgd2=un3=ac3=gd3=vgd3=0

for i in range(0,1150):
    if train[i][3]=='more':
        if train[i][6]=='unacc':
            un0 += 1
        elif train[i][6]=='acc':
            ac0 += 1
        elif train[i][6]=='good':
            gd0 += 1
        elif train[i][6]=='vgood':
            vgd0 += 1
    elif train[i][3]=='4':
        if train[i][6]=='unacc':
            un1 += 1
        elif train[i][6]=='acc':
            ac1 += 1
        elif train[i][6]=='good':
            gd1 += 1
        elif train[i][6]=='vgood':
            vgd1 += 1
    elif train[i][3]=='2':
        if train[i][6]=='unacc':
            un2 += 1
        elif train[i][6]=='acc':
            ac2 += 1
        elif train[i][6]=='good':
            gd2 += 1
        elif train[i][6]=='vgood':
            vgd2 += 1
persons=[[vgd0,gd0,ac0,un0],[vgd1,gd1,ac1,un1],[vgd2,gd2,ac2,un2]]
un0=ac0=gd0=vgd0=un1=ac1=gd1=vgd1=un2=ac2=gd2=vgd2=un3=ac3=gd3=vgd3=0

for i in range(0,1150):
    if train[i][4]=='big':
        if train[i][6]=='unacc':
            un0 += 1
        elif train[i][6]=='acc':
            ac0 += 1
        elif train[i][6]=='good':
            gd0 += 1
        elif train[i][6]=='vgood':
            vgd0 += 1
    elif train[i][4]=='med':
        if train[i][6]=='unacc':
            un1 += 1
        elif train[i][6]=='acc':
            ac1 += 1
        elif train[i][6]=='good':
            gd1 += 1
        elif train[i][6]=='vgood':
            vgd1 += 1
    elif train[i][4]=='small':
        if train[i][6]=='unacc':
            un2 += 1
        elif train[i][6]=='acc':
            ac2 += 1
        elif train[i][6]=='good':
            gd2 += 1
        elif train[i][6]=='vgood':
            vgd2 += 1
lboot=[[vgd0,gd0,ac0,un0],[vgd1,gd1,ac1,un1],[vgd2,gd2,ac2,un2]]
un0=ac0=gd0=vgd0=un1=ac1=gd1=vgd1=un2=ac2=gd2=vgd2=un3=ac3=gd3=vgd3=0

for i in range(0,1150):
    if train[i][5]=='high':
        if train[i][6]=='unacc':
            un0 += 1
        elif train[i][6]=='acc':
            ac0 += 1
        elif train[i][6]=='good':
            gd0 += 1
        elif train[i][6]=='vgood':
            vgd0 += 1
    elif train[i][5]=='med':
        if train[i][6]=='unacc':
            un1 += 1
        elif train[i][6]=='acc':
            ac1 += 1
        elif train[i][6]=='good':
            gd1 += 1
        elif train[i][6]=='vgood':
            vgd1 += 1
    elif train[i][5]=='low':
        if train[i][6]=='unacc':
            un2 += 1
        elif train[i][6]=='acc':
            ac2 += 1
        elif train[i][6]=='good':
            gd2 += 1
        elif train[i][6]=='vgood':
            vgd2 += 1
safe=[[vgd0,gd0,ac0,un0],[vgd1,gd1,ac1,un1],[vgd2,gd2,ac2,un2]]
un0=ac0=gd0=vgd0=un1=ac1=gd1=vgd1=un2=ac2=gd2=vgd2=un3=ac3=gd3=vgd3=0

for i in range(0,1150):
    if train[i][6]=='unacc':
        un0 += 1
    elif train[i][6]=='acc':
        ac0 += 1
    elif train[i][6]=='good':
        gd0 += 1
    elif train[i][6]=='vgood':
        vgd0 += 1
clas=[vgd0,gd0,ac0,un0]

del un0,ac0,gd0,vgd0,un1,ac1,gd1,vgd1,un2,ac2,gd2,vgd2,un3,ac3,gd3,vgd3,i,z,data


from math import log
def entropy(pi):
    total = 0
    for p in pi:
        p = p / sum(pi)
        if p != 0:
            total += p * log(p, 2)
        else:
            total += 0
    total *= -1
    return total

def gain(d, a):
    total = 0
    for v in a:
        total += sum(v) / sum(d) * entropy(v)

    gain = entropy(d) - total
    return gain

def intl(d,a):
    total=0
    for v in a:
        total += sum(v) / sum(d) * log(  (sum(v)/sum(d)) , 2 )
    total *= -1
    return total

def gainrat(d,a):
    return gain(d,a)/intl(d,a)

def gin(pi):
    total = 0
    for p in pi:
        p = p / sum(pi)
        total += p * p
    gi = 1 - total
    return gi

def gini(d,a):
    total = 0
    for v in a:
        total += sum(v) / sum(d) * gin(v)
    return total


    
    
print('Gains:buy     ',gain(clas, buy))
print('      maint   ',gain(clas, maint))
print('      doors   ',gain(clas, doors))
print('      persons ',gain(clas, persons))
print('      lboot   ',gain(clas, lboot))
print('      safe    ',gain(clas, safe),'\n')

print('Ratios:buy    ', gainrat(clas, buy))
print('       maint  ',gainrat(clas, maint))
print('       doors  ',gainrat(clas, doors))
print('       persons',gainrat(clas, persons))
print('       lbot   ',gainrat(clas, lboot))
print('       safe   ',gainrat(clas, safe),'\n')

print('Ginis: buy    ', gini(clas, buy))
print('       maint  ',gini(clas, maint))
print('       doors  ',gini(clas, doors))
print('       persons',gini(clas, persons))
print('       lboot  ',gini(clas, lboot))
print('       safe   ',gini(clas, safe))

