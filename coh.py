import csv 
from pathlib import Path 
 
coh_path= Path.cwd()/"csv_reports"/"cash_on_hand.csv" 
 
coh_list = [] 
coh_amount = [] 
 
with coh_path.open(mode = "r", encoding = "UTF-8", newline = "") as file : 
    readfiles = csv.reader(file) 
    next(readfiles) 
    for line in readfiles:  
        coh_list.append(line)
        coh_amount.append(float(line[1]))

summary_path = Path.cwd()/"summary_reports.txt"

def coh_difference(rate):
    for number in range(0,(len(coh_amount)-1)):
        first_day = coh_amount[number]
        second_day = coh_amount[number+1]
        if first_day > second_day:
            difference = first_day - second_day
            difference_sgd = difference * rate
            difference_day = coh_list[number+1][0]
            with summary_path.open(mode='a',encoding='UTF-8') as file:
                file.write(f"[CASH DEFICIT] DAY{difference_day}, AMOUNT : SGD{difference_sgd}")


        