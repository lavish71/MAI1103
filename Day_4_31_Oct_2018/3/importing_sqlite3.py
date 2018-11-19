# Importing Library SQLITE of version 3 and CSV
import sqlite3
import csv

db = sqlite3.connect('csv.db')
c = db.cursor()

# Inputs
print ("For Zoo db enter 1")
print ("For student db enter 2")
print ("For cars db enter 3")
database = input("Choose your database : ")

# Reading zoo.csv file
if(database == 1):
    #c.execute("""CREATE TABLE zoo(animal TEXT,id INTEGER,water_need INTEGER)""")
    with open('zoo.csv') as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            c.execute("""INSERT INTO zoo(animal,id,water_need)
                        VALUES('{}',{},{})""".format(row[0],row[1],row[2]))
    c.execute("""SELECT * FROM zoo""")
    show = (c.fetchall())
    for a in show:
        print a[0]," ",a[1]," ",a[2]

# Reading students.csv file
elif(database == 2):
    #c.execute("""CREATE TABLE student(FirstName TEXT,Grade INTEGER,Classroom INTEGER)""")
    with open('students.csv') as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            c.execute("""INSERT INTO student(FirstName,Grade,Classroom)
                        VALUES('{}',{},{})""".format(row[0],row[1],row[2]))
    c.execute("""SELECT * FROM student""")
    show = (c.fetchall())
    for a in show:
        print a[0]," ",a[1]," ",a[2]

# Reading carmakers.csv file
elif(database == 3):
    #c.execute("""CREATE TABLE cars(Maker TEXT,FullName TEXT,Country INTEGER)""")
    with open('carmakers.csv') as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=';')
        next(csv_reader)
        for row in csv_reader:
            c.execute("""INSERT INTO cars(Maker,FullName,Country)
                        VALUES({},{},{})""".format(row[0],row[1],row[2]))
    c.execute("""SELECT * FROM cars""")
    show = (c.fetchall())
    for a in show:
        print a[0]," ",a[1]," ",a[2]
        
# To skip the header from csv file
# Inserting values in the Table
# Executing all data from Table
