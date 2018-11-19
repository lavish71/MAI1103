# Importing Library "Operating System"
import os

# Changing directory
os.chdir('D:\Luv\Lavish_Sharma\Python\Day2_Wed_24_Oct_2018')
count = 0

# Importing Library "csv"
import csv

# Reading zoo.csv file
with open('zoo.csv') as csv_data:
    csv_reader = csv.reader(csv_data, delimiter=',')

    # To skip the header from csv file
    next(csv_reader)
    
    # To print total water need for all animals
    for row in csv_reader:
        print row[0],row[2]
        count += int(row[2])
    # Printing total water need for all animals
    print("Total water needed : {}".format(count))
