import math

file = open('tunnel times fuller set.csv')
data_file = file.read()
data_file = data_file.replace(',', '\n')
data_list = data_file.split()
print(data_list)

east_camera = 185
west_camera = 105

for i in range(0, len(data_list)//2, 2):
    duplicate = [a for a, val in enumerate(data_list) if val == data_list[i]] #pairs the duplicate number plates in a list

    enter = data_list[duplicate[0]+1]
    enter = enter.split(':')
    for i in range(len(enter)):
        enter[i] = int(enter[i])
    enter_sec = (enter[0]*3600)+(enter[1]*60)+(enter[2])

    exit = data_list[duplicate[1]+1]
    exit = exit.split(':')
    for i in range(len(exit)):
        exit[i] = int(exit[i])
    exit_sec = (exit[0]*3600)+(exit[1]*60)+(exit[2])

    travel_time = exit_sec - enter_sec
    speed_ms = (2400+east_camera+west_camera)/travel_time
    speed_kmh = speed_ms*3.6
    speed_kmh = math.floor(speed_kmh)
    print(speed_kmh)
