"""
data_find_avg.py
METU CENG499 Project
Author : Cemal Erat
Date(dd/mm/yyy): 20/05/2018
Description : Calculates BLK% and STL% Regular season averages of teams
"""

inputfile = open('data1718.txt')
outputfile = open('out1718.txt', 'w')

lines = [line.rstrip('\n') for line in inputfile]

teams = {"tor":[0.0,0.0], "bos":[0.0,0.0], "phi":[0.0,0.0], "nyk":[0.0,0.0], "brk":[0.0,0.0],
            "por":[0.0,0.0], "okc":[0.0,0.0], "uta":[0.0,0.0], "min":[0.0,0.0], "den":[0.0,0.0],
            "cle":[0.0,0.0], "ind":[0.0,0.0], "mil":[0.0,0.0], "det":[0.0,0.0], "chi":[0.0,0.0],
            "gsw":[0.0,0.0], "lac":[0.0,0.0], "lal":[0.0,0.0], "sac":[0.0,0.0], "pho":[0.0,0.0],
            "mia":[0.0,0.0], "was":[0.0,0.0], "cho":[0.0,0.0], "orl":[0.0,0.0], "atl":[0.0,0.0],
            "hou":[0.0,0.0], "nop":[0.0,0.0], "sas":[0.0,0.0], "dal":[0.0,0.0], "mem":[0.0,0.0]}

for i in lines:
    line = i.split()
    home = line[0][8:11]
    away = line[0][11:14]
    stl_home = float(line[8])
    blk_home = float(line[9])
    stl_away = float(line[18])
    blk_away = float(line[19])
    teams[home][0] += stl_home
    teams[home][1] += blk_home
    teams[away][0] += stl_away
    teams[away][1] += blk_away

for i in teams:
    teams[i][0] = round(teams[i][0]/82,1)
    teams[i][1] = round(teams[i][1]/82,1)
    # [team-name] [BLK%] [STL%]
    print(i,teams[i][1],teams[i][0], file=outputfile)

