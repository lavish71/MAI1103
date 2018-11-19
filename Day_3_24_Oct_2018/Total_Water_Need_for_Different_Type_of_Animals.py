# Taking some variables to get total water needed  for different type of animals
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

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

    # To print total water need for different type of animals
    for row in csv_reader:
        if row[0]=="elephant":
            count1+=int(row[2])
        if row[0]=="tiger":
            count2+=int(row[2])
        if row[0]=="zebra":
            count3+=int(row[2])
        if row[0]=="lion":
            count4+=int(row[2])
        if row[0]=="kangaroo":
            count5+=int(row[2])
    # Printing total water need for Elephant
    print("Total water needed by Elephant is {}".format(count1))
    # Printing total water need for Tiger
    print("Total water needed by Tiger is {}".format(count2))
    # Printing total water need for Zebra
    print("Total water needed by  Zebra is {}".format(count3))
    # Printing total water need for Lion
    print("Total water needed by  Lion is {}".format(count4))
    # Printing total water need for Kangaroos
    print("Total water needed by  Kangaroo is {}".format(count5))
