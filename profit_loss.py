from ast import Return
import csv
from pathlib import Path

# create a file path to "profits and loss.csv" file 
profit_loss_file = Path.cwd()/"csv_reports"/"Profits and Loss.csv"

# create 2 empty lists to store data into the list
profit_loss_list = []
pnl_amount = []

# using .open() function to access mode of file which is for reading the csv file, 
# encoding which is to include longer or all characters and save files as profit_loss
with profit_loss_file.open(mode = "r", encoding = "UTF-8", newline = "") as profit_loss :
    # using .reader() function in csv module to read the data in profit-loss file
    readfiles = csv.reader(profit_loss)
    # using .next() function to return the next item in the list
    next(readfiles)

    # apply for loop to create a list comprehension expression
    for line in readfiles: 
        # using .append() function to add read files into the list
        profit_loss_list.append(line)
        # using .append() function to add the amount into the  list and convert it to a float
        # using index[4] to extract only the amount in the 4th index which is the net profit
        pnl_amount.append(float(line[4]))

# create another filepath to the "summary_reports.txt" file
summary_path = Path.cwd()/"summary_reports.txt"

# define the rate variable
def pnl_difference(rate):
    # using len(pnl_amount)-1 is because there are 6 days but we only want the range from 0 to 5
    for number in range(0,(len(pnl_amount)-1)):
        # first day amount is [number] because is in the 0 index
        first_day = pnl_amount[number]
        # second day amount is [number+1] because is in the 1 index
        second_day = pnl_amount[number+1]

        if first_day > second_day:
            # find the difference between the amount of the first day and second day
            difference = first_day - second_day
            # use the difference result multiply by the rate to get the amount after the exchange rate
            difference_sgd = difference * rate
            difference_day = profit_loss_list[number+1][0]
            # open the file for appending 
            with summary_path.open (mode= 'a', encoding= 'UTF-8') as file:
                # using .write() function to write the results on the summary report
                file.write(f"[PROFIT DEFICIT] DAY{difference_day}, AMOUNT : SGD{round(difference_sgd,2)}" + "\n")