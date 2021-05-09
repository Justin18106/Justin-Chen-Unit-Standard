file = open('tunneldata.txt.csv')
data_file = file.read()
data_file = data_file.replace(',', '\n')
data_list = data_file.split()
print(data_list)

fine_amount = [30, 80, 120, 170, 230, 300, 400, 510, 630]
