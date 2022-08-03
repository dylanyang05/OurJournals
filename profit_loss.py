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

#print(profit_loss_list)

el= []
el2= []
for numbers in profit_loss_list:
   day = numbers[0]
   amount = numbers[4]
   el.append(day)
   el2.append(amount)
   #print(el)
   #print(el2)
   print(slice(amount))


