import csv
from pathlib import Path
from unicodedata import category

#Create file path to overheads csv file
Overheads_file= Path.cwd()/"csv_reports"/"Overheads.csv"

#Create an empty list to store data into the list 
OurJournals_Overheads_list=[]
final_Overheadslist= []

#Using the .open() funtion to acess mode of file which is for reading the csv file, encoding which is to inclue longer/all characters and save files as overheads
with Overheads_file.open (mode="r", encoding= "UTF-8") as Overheads:
    
#Using .reader() function in csv module to read the data in overheads file
    readfiles= csv.reader(Overheads)

#Using next() function to return the next item in the list
    next(readfiles)

#Apply for loop to create a list comprehension expression since there is 2 items in each tuple, largest value and list that consist of different expenses
    for line in readfiles:
        OurJournals_Overheads_list.append(line)
        final_Overheadslist.append(float(line[1]))

print(OurJournals_Overheads_list)        
print(final_Overheadslist)

highestvalue=max(final_Overheadslist)
for information in OurJournals_Overheads_list:
    if information[1] == str(highestvalue):
        highest_overhead=information[0]

def highestOverheads_details():
    message= (f"[HIGHEST OVERHEADS]: {highest_overhead}, AMOUNT: SGD{highestvalue}")
    print (message)
highestOverheads_details()
print("hi")