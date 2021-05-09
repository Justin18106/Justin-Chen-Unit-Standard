import math

file = open('tunnel times fuller set.csv')
datafile = file.read()
datafile = datafile.replace(',', '\n')
datalist = datafile.split()

x = 5
y = -1
fine = [30, 80, 120, 170, 230, 300, 400, 510, 630]
speedfine = {1:30, 2:30, 3:30, 4:30, 5:30}
for i in range(9):
    y = y+1
    for i in range(5):
        x = x+1
        speedfine[x] = fine[y]

eastcamera = 185
westcamera = 105

speedlimit = int(input('What is the speed limit? '))

for i in range(0, len(datalist)//2, 2):
    duplicate = [a for a, val in enumerate(datalist) if val == datalist[i]] #pairs the duplicate number plates in a list

    enter = datalist[duplicate[0]+1]
    enter = enter.split(':')
    for i in range(len(enter)):
        enter[i] = int(enter[i])
    entersecond = (enter[0]*3600)+(enter[1]*60)+(enter[2])

    exit = datalist[duplicate[1]+1]
    exit = exit.split(':')
    for i in range(len(exit)):
        exit[i] = int(exit[i])
    exitsecond = (exit[0]*3600)+(exit[1]*60)+(exit[2])

    traveltime = exitsecond - entersecond
    speedms = (2400+eastcamera+westcamera)/traveltime
    speedkmh = speedms*3.6
    speedkmh = math.floor(speedkmh)

    overlimit = speedkmh - speedlimit
    if overlimit > 0:
        print('Carplate:', datalist[duplicate[0]])
        print('Speed:', speedkmh, 'km/h')        
        if overlimit <= 50:
            print('Fine: $', speedfine[overlimit], '\n')
        else:
            print('Fine: $', fine[8],'\n')
