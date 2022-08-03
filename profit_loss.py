from ast import Return
import csv
from pathlib import Path

profit_loss_file = Path.cwd()/"csv_reports"/"Profits and Loss.csv"

profit_loss_list = []
pnl_amount = []

with profit_loss_file.open(mode = "r", encoding = "UTF-8", newline = "") as profit_loss :
    readfiles = csv.reader(profit_loss)
    next(readfiles)
    for line in readfiles: 
        profit_loss_list.append(line)
        pnl_amount.append(float(line[4]))

summary_path = Path.cwd()/"summary_reports.txt"

def pnl_difference(rate):
    for number in range(0,(len(pnl_amount)-1)):
        first_day = pnl_amount[number]
        second_day = pnl_amount[number+1]
        if first_day > second_day:
            difference = first_day - second_day
            difference_sgd = difference * rate
            difference_day = profit_loss_list[number+1][0]
            with summary_path.open (mode= 'a', encoding= 'UTF-8') as file:
                file.write(f"[PROFIT DEFICIT] DAY{difference_day}, AMOUNT : SGD{round(difference_sgd,2)}" + "\n")


