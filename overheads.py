import csv
from pathlib import Path


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

#Apply for loop to create a list comprehension expression since there is 2 items in each tuple, largest value and list 
    for line in readfiles:
        #Using the append function to add read files into the list
        Overheads_list.append(line)
        #Using the append function to add the amount into the list and covert it into float
        Overheads_amount.append(float(line[1]))

#Finding the highest value using max() function from the amount list
highestvalue=max(Overheads_amount)
#Apply for loop to create a list comprehension expression since there is 2 items in each tuple, information we have gathered from finding the highest value and list 
for information in Overheads_list:
    #Using if function to match the value to the overhead list
    if information[1] == str(highestvalue):
        #Assign 'highest overhead' name to the information extracted
        highest_overhead=information[0]

#Create another filepath to the summary report txt file and assign it as summary_path
summary_path= Path.cwd()/"summary_reports.txt"

#Define the rate varible 
def Overheads_details(rate):
    #Multiply the highest value by the rate to get the final amount
    highestvalue_sgd= highestvalue*rate
    #Create message for the highest overhead output followed by the final amount
    message= (f"[HIGHEST OVERHEADS]: {highest_overhead}: SGD{round(highestvalue_sgd,2)}")
    #Using the .open() function to append to the final txt file and encoding which is to include longer/all characters and save it as file
    with summary_path.open (mode="a", encoding= "UTF-8") as file:
        #Using .write() function to write the message into the final txt file
        file.write(message + "\n")
        #Using .close function to close file to prevent issues of corrupted data
        file.close()
