"""
playoff_sim.py
METU CENG499 Project
Author : Cemal Erat
Date(dd/mm/yyy): 20/05/2018
Description : Playoff simulator
"""

inputfile = open('sim_input.txt')
reginput = open('data_16_17_rseason_avg.txt')
outputfile = open('sim_output.txt', 'w')

lines = [line.rstrip('\n----------------------------------') for line in inputfile]
lines_reg = [line.rstrip('\n----------------------------------') for line in reginput]

# placeholder match prediction
def play(m1,m2):
    return m1[0:3]+m2[0:3]

def search(match):
    home = match[0:3]
    away = match[3:6]
    home_stats = ''
    away_stats = ''
    for i in lines_reg:
        line = i.split()
        if line[0] == home:
            home_stats = i[4:]
        if line[0] == away:
            away_stats = i[4:]
    print(home+away,home_stats,away_stats)
    print(home+away,home_stats,away_stats, file=outputfile)


matches = []

for i in lines:
    line = i.split()
    match = line[0]+line[1]
    matches.append(match)

# east first round
print("\n\n### east first round ###")
print(matches[0],matches[1],matches[2],matches[3],'\n----------------------------------')
for i in range(0,4):
    search(matches[i])
matches[0] = play(matches[0],matches[3])
matches[1] = play(matches[1],matches[2])
print('----------------------------------\n',matches[0],matches[1])

# west first round
print("\n\n### west first round ###")
print(matches[4],matches[5],matches[6],matches[7],'\n----------------------------------')
for i in range(4,8):
    search(matches[i])
matches[2] = play(matches[4],matches[7])
matches[3] = play(matches[5],matches[6])
print('----------------------------------\n',matches[4],matches[5])

# east second round
print("\n\n### east second round ###")
print(matches[0],matches[1],'\n----------------------------------')
for i in range(0,2):
    search(matches[i])
matches[0] = play(matches[0],matches[1])
print('----------------------------------\n',matches[0])

# west second round
print("\n\n### west second round ###")
print(matches[2],matches[3],'\n----------------------------------')
for i in range(2,4):
    search(matches[i])
matches[1] = play(matches[2],matches[3])
print('----------------------------------\n',matches[1])

# conference finals (need to determine home court adv)
print("\n\n### conference finals ###")
print(matches[0],matches[1],'\n----------------------------------')
for i in range(0,2):
    search(matches[i])
matches[0] = play(matches[0],matches[1])
print('----------------------------------\n',matches[0])

# finals
print("\n\n### finals ###")
print(matches[0],'\n----------------------------------')
search(matches[0])

