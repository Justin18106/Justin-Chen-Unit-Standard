import math


count1 = 5
count2 = -1
fine = [30, 80, 120, 170, 230, 300, 400, 510, 630]
speedfine = {1: 30, 2: 30, 3: 30, 4: 30, 5: 30}
for i in range(len(fine)):  # repeats the code for each fine value
    count2 = count2+1
    for i in range(5):
        count1 = count1+1
        speedfine[count1] = fine[count2]  # pairs a speed over the limit with a fine

fourminutes = []  # list for cars that have not exited within 4 minutes

once = []

eastcamera = 185
westcamera = 105


def openfile():  # opens and converts data file into list
    global datalist
    filename = input('What file would you like to open? ')  # tunnel times fuller set.csv / testdatacomma.txt / tnnel test times.txt
    try:
        file = open(filename)
        datafile = file.read()
        datafile = datafile.replace(',', '\n')
        datalist = datafile.split()
    except:
        openfile()


def validate(x):  # ensures input is a positive integer
    global y
    try:
        y = int(x)
        if y < 1:
            x = input('Please enter a positive number: ')
            validate(x)
    except:
        x = input('Please enter an integer: ')
        validate(x)


def speed():
    speedlimit = input('\nWhat is the speed limit? (km/h): ')
    validate(speedlimit)
    speedlimit = int(y)
    try:
        for i in range(0, len(datalist), 2):  # repeats the code for every second element in datalist
            duplicate = [a for a, val in enumerate(datalist) if val == datalist[i]]  # pairs the duplicate number plates in a list
            if len(duplicate) > 1:

                duplicateindex = [x for x in range(len(datalist)) if datalist[x] == datalist[duplicate[0]]]

                enter = datalist[duplicate[0]+1]  # finds the values after the first element in the pair
                enter = enter.split(':')
                for i in range(len(enter)):  # converts the values of the time into integers
                    enter[i] = int(enter[i])
                entersecond = (enter[0]*3600)+(enter[1]*60)+(enter[2])  # converts the enter time into seconds

                exit = datalist[duplicate[1]+1]  # finds the values after the second element in the pair
                exit = exit.split(':')
                for i in range(len(exit)):
                    exit[i] = int(exit[i])
                exitsecond = (exit[0]*3600)+(exit[1]*60)+(exit[2])

                traveltime = exitsecond - entersecond
                if traveltime > 240:  # add cars that take over 4 minutes to exit the tunnel to a list
                    fourminutes.append(datalist[duplicate[0]])

                try:  # calculates the average speed of the car
                    speedms = (2400+eastcamera+westcamera)/traveltime
                except:
                    continue

                speedkmh = speedms*3.6  # converts the speed to kilometers per hour
                speedkmh = math.floor(speedkmh)  # rounds the speed down

                overlimit = speedkmh - speedlimit
                if overlimit > 0:  # prints data if speed is over limit
                    print('\nCarplate:', datalist[duplicate[0]])
                    print('Enter Time:', datalist[duplicate[0]+1])
                    print('Exit Time:', datalist[duplicate[1]+1])
                    print('Speed:', speedkmh, 'km/h')
                    if overlimit <= 50:
                        print('Fine: $', speedfine[overlimit])
                    else:
                        print('Fine: $', fine[8])

                datalist.pop(duplicateindex[1]+1)
                datalist.pop(duplicateindex[1])

            else:
                once.append(datalist[duplicate[0]])
    except:
        pass

    print('\nThese cars have not exited within 4 minutes:\n', fourminutes)
    print('\nThese cars have no exited the tunnel:\n', once)
    print()


def rerun():
    while True:
        while True:
            answer = input('Would you like to rerun the program? (yes/no): ')
            answer = answer.lower()
            if answer in ('yes', 'no'):
                break
        if answer == 'yes':
            fourminutes.clear()
            once.clear()
            print()
            openfile()
            speed()
        else:
            print("\nExiting program...")
            break


openfile()
speed()
rerun()
