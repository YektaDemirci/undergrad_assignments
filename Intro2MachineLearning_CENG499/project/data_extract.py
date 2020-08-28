"""
dataextract.py
METU CENG499 Project
Author : Burak Kaan Bilgehan, Yekta Demirci (yektademirci@hotmail.com), İlayda Beyreli(ilaydabeyreli@gmail.com)
Date(dd/mm/yyy): 02/05/2018
Description : Extracting the NBA statistics and constructing the training and test data sets using BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup

f = open("data.txt", "w")
print("The file : data is opened.")

base = "https://www.basketball-reference.com/boxscores/"
# game dates for 2017/2018  season
date = ["201710"  , "201711", "201712", "201801", "201802", "201803", "201804", "201805"]

day = []
for i in range (1,32):
    day.append(str(i).zfill(2))
for i in day:
    print(i)
bit = "0"
# 30 teams
team = ("TOR", "BOS", "PHI", "NYK", "BRK",
        "POR", "OKC", "UTA", "MIN", "DEN",
        "CLE", "IND", "MIL", "DET", "CHI",
        "GSW", "LAC", "LAL", "SAC", "PHO",
        "MIA", "WAS", "CHO", "ORL", "ATL",
        "HOU", "NOP", "SAS", "DAL", "MEM")
extend = ".html" # regular html extention

box = "box_"
teamstat = ("tor", "bos", "phi", "nyk", "brk",
            "por", "okc", "uta", "min", "den",
            "cle", "ind", "mil", "det", "chi",
            "gsw", "lac", "lal", "sac", "pho",
            "mia", "was", "cho", "orl", "atl",
            "hou", "nop", "sas", "dal", "mem")

advanced = "_advanced"
y = 0 # result
numbers_home = []
numbers_road = []
print("Base parameters are set.\nThe extraction is initiated.")
for m in date:
    print(m)
    for d in day:
        for t in team:
            r = requests.get(base+m+d+bit+t+extend)
            # print(r.url)
            # print(base+year+m+d+bit+t+extend) # html page that has been reached
            soup = BeautifulSoup(r.content, "html.parser")
            score = soup.find_all("div", {"class": "score"})
            if (len(score) != 0):
                numbers = [int(number.contents[0]) for number in score]
                if(numbers[0] > numbers[1]): #if road wins
                    y = 0;
                elif (numbers[0] < numbers[1]): # if home wins
                    y = 1;
             # the road team is the same with the html string 
            t_home = t.lower()
            games_home = soup.find_all("table", {"id": box+t_home+advanced})
            if(len(games_home) != 0):
                stats_home = (games_home[0].contents)[8]
                stats_home = stats_home.find_all("td", {"class": "right"})
                # getting the numbers
                numbers_home = [float(number.contents[0]) for number in stats_home]
                # searching for the home team
                for t_road in teamstat:
                    if (t_road != t_home): # ignore the self-match
                        games_road = soup.find_all("table", {"id": box+t_road+advanced})
                        if (len(games_road) != 0):
                            stats_road = (games_road[0].contents)[8]
                            stats_road = stats_road.find_all("td", {"class": "right"})

                            # getting the numbers
                            numbers_road = [float(number.contents[0]) for number in stats_road]
                            # printing the home team stats
                            f.write(m)
                            f.write(d)
                            # print(d)
                            # print(t_home)
                            f.write(t_home)
                            f.write(t_road)
                            for i in range (0,len(numbers_home)):
                                if( i != 0 and i != 7 and i != 12 and i != 13 and i != 14):
                                    # print(format(numbers_home[i]))
                                    # print(" ")
                                    f.write(format(numbers_home[i]))
                                    f.write(" ")
                            # printing the road team stats
                            # print(t_road)
                            for i in range (0, len(numbers_road)):
                                if (i != 0 and i != 7 and i != 12 and i != 13 and i != 14):
                                    # print(format(numbers_road[i]))
                                    # print(" ")
                                    f.write(format(numbers_road[i]))
                                    f.write(" ")
                            # print(format(y))
                            # print("\n")
                            f.write(format(y))
                            f.write("\n")

print("Data extract is done!")
f.close()
print("File is closed!")

