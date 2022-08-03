import csv
from pathlib import Path
from unicodedata import category

#Create file path to overheads csv file
Overheads_file= Path.cwd()/"csv_reports"/"Overheads.csv"

#Create an empty list to store data into the list 
OurJournals_Overheads_list=[]

#Using the .open() funtion to acess mode of file which is for reading the csv file, encoding which is to inclue longer/all characters and save files as overheads
with Overheads_file.open (mode="r", encoding= "UTF-8") as Overheads:
    
#Using .reader() function in csv module to read the data in overheads file
    readfiles= csv.reader(Overheads)

#Using next() function to return the next item in the list
    next(readfiles)

#Apply for loop to create a list comprehension expression since there is 2 items in each tuple, largest value and list that consist of different expenses
    for line in readfiles:

#Using append function to access largest value of the nested list to the empty list
        OurJournals_Overheads_list.append(line[1])

#Create another empty list to store the final data        
final_Overheadslist= []

#Apply for loop to create a list 
for information in OurJournals_Overheads_list:

#Convert the info into float 
    information= float(information)
    final_Overheadslist.append(information)

print(final_Overheadslist)

def highestOverheads_details():

    #for overheaddetails in final_Overheadslist:
        #if overheaddetails> highestvalue:
            highestvalue=max(final_Overheadslist)
            #index=(final_Overheadslist.index(highestvalue))
            message= (f"[HIGHEST OVERHEADS]:", highestvalue)
            return message

print (highestOverheads_details())