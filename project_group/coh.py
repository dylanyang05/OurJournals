import csv 
from pathlib import Path 

# create a file path to "cash_on_hand" file 
coh_path= Path.cwd()/"csv_reports"/"cash_on_hand.csv" 

# create 2 empty lists to store data into the list
coh_list = [] 
coh_amount = [] 

# using .open() function to access mode of file which is for reading the csv file, 
# encoding which is to include longer or all characters and save files as file
with coh_path.open(mode = "r", encoding = "UTF-8", newline = "") as file : 
    # using .reader() function in csv module to read the data in file
    readfiles = csv.reader(file) 
    # using .next() function to return the next item in the list
    next(readfiles) 

    # apply for loop to create a list comprehension expression
    for line in readfiles:  
        # using .append() function to add read files into the list
        coh_list.append(line)
        # using .append() function to add the amount into the list and convert it to a float
        # using index[1] to extract only the amount in the 1st index which is the cash on hand
        coh_amount.append(float(line[1]))

# create another filepath to the "summary_reports.txt" file
summary_path = Path.cwd()/"summary_reports.txt"

# define the rate variable
def coh_difference(rate):
    # using len(coh_amount)-1 is because there are 6 days but we only want the range from 0 to 5
    for number in range(0,(len(coh_amount)-1)):
        # first day amount is [number] because is in the 0 index
        first_day = coh_amount[number]
        # second day amount is [number+1] because is in the 1 index
        second_day = coh_amount[number+1]

        if first_day > second_day:
            # find the difference between the amount of the first day and second day
            difference = first_day - second_day
            # use the difference result multiply by the rate to get the amount after the exchange rate
            difference_sgd = difference * rate
            difference_day = coh_list[number+1][0]
            # open the file for appending
            with summary_path.open(mode='a',encoding='UTF-8') as file:
                # using .write() function to write the results on the summary report
                file.write(f"[CASH DEFICIT] DAY{difference_day}, AMOUNT : SGD{round(difference_sgd,2)}" + "\n")


        