# Importing Library "SQLITE of version 3"
import sqlite3

# Importing Library "csv"
import csv

# Connecting/Creating to Database
db = sqlite3.connect('zoo.db')

#Creating Cursor
c=db.cursor()

# Reading zoo.csv file
with open('zoo.csv') as csv_data:
    csv_reader = csv.reader(csv_data, delimiter=',')
    
    # To skip the header from csv file
    next(csv_reader)

    # Inserting values in the Table
    for row in csv_reader:
        c.execute("""INSERT INTO zoo(animal,id,water_need)
                        VALUES('{}',{},{})""".format(row[0],row[1],row[2]))

# Executing all data from Table
c.execute("""SELECT * FROM zoo""")
show = (c.fetchall())
for a in show:
    print a[0]," ",a[1]," ",a[2]
