from ast import Return
import csv
from pathlib import Path

profit_loss_file = Path.cwd()/"csv_reports"/"Profits and Loss.csv"

profit_loss_list = []
final_pnl_list = []

with profit_loss_file.open(mode = "r", encoding = "UTF-8", newline = "") as profit_loss :
    readfiles = csv.reader(profit_loss)
    next(readfiles)
    for line in readfiles: 
        profit_loss_list.append(line)
        final_pnl_list.append(float(line[4]))

print(profit_loss_list)
print(final_pnl_list)

for amount in final_pnl_list :
    index = 1
    if amount[index] > amount[[index-1]] :
        print(amount[index] - amount[index-1])



#if final_pnl_list[1] < final_pnl_list[0] :

#print("The profit and loss on Day 41 is lower than Day 40 by", abs(difference1))
#print("The profit and loss on Day 43 is lower than Day 42 by", (difference2))
#print("The profit and loss on Day 45 is lower than Day 44 by", (difference3))