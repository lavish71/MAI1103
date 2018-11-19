# Importing Library "SQLITE of version 3"
import mysql.connector

# Importing Library "csv"
import csv

# Connecting/Creating to Database
db = mysql.connector.connect(user='root', password='Bsdu@123', host='localhost')

#Creating Cursor
c=db.cursor()

#Creating Database
#c.execute("""CREATE DATABASE jungle""")
c.execute("""USE DATABASE jungle""")
c.execute("""CREATE TABLE anim(animal TEXT,id INTEGER,water_need INTEGER)""")
        
# Reading zoo.csv file
with open('zoo.csv') as csv_data:
    csv_reader = csv.reader(csv_data, delimiter=',')
    
    # To skip the header from csv file
    next(csv_reader)

    # Inserting values in the Table
    for row in csv_reader:
        c.execute("""INSERT INTO anim(animal,id,water_need)
                        VALUES('{}',{},{})""".format(row[0],row[1],row[2]))

# Executing all data from Table
c.execute("""SELECT * FROM anim""")
show = (c.fetchall())
for a in show:
    print a[0]," ",a[1]," ",a[2]
