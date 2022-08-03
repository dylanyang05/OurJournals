import csv
from pathlib import Path
from unicodedata import category

#Create file path to overheads csv file
Overheads= Path.cwd()/"csv_reports"/"Overheads.csv"

#Create an 2 empty list to store data into the list 
Overheads_list=[]
Overheads_amount= []

#Using the .open() funtion to acess mode of file which is for reading the csv file, encoding which is to inclue longer/all characters and save files as overheads
with Overheads.open (mode="r", encoding= "UTF-8") as file:
    
#Using .reader() function in csv module to read the data in overheads file
    readfiles= csv.reader(file)

#Using next() function to return the next item in the list
    next(readfiles)

#Apply for loop to create a list comprehension expression since there is 2 items in each tuple, largest value and list that consist of different expenses
    for line in readfiles:

#Using the append function to add read files into the list
        Overheads_list.append(line)

#A
        Overheads_amount.append(float(line[1]))

highestvalue=max(Overheads_amount)
for information in Overheads_list:
    if information[1] == str(highestvalue):
        highest_overhead=information[0]

def Overheads_details():
    message= (f"[HIGHEST OVERHEADS]: {highest_overhead}: SGD{highestvalue}")
    print (message)
Overheads_details()
