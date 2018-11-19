# Taking some variables to get total water needed  for different type of animals
count = 0
anim = {}
# Importing Library "Operating System"
import os

# Changing directory
os.chdir('D:\Luv\Lavish_Sharma\Python\Day2_Wed_24_Oct_2018')

# Importing Library "csv"
import csv

# Reading zoo.csv file
with open('zoo.csv') as csv_data:
    csv_reader = csv.reader(csv_data, delimiter=',')
    
    # To skip the header from csv file
    next(csv_reader)

    # Using dictionary in for loop
    for row in csv_reader:
        if row[0] not in anim.keys():
            anim[row[0]] = int(row[2])
        else:
            anim[row[0]] = anim[row[0]] + int(row[2])
print anim
for key, values in anim.items():
    print(key,values)
