# Importing Library "Operating System"
import os

# Changing directory
os.chdir('D:\Luv\Lavish_Sharma\Python\Day2_Wed_24_Oct_2018')

#Current WOrking Directory
print os.getcwd()

# Reading zoo.csv file
with open('zoo.csv', 'rt') as zoo:
    print zoo.read()
