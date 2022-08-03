from ast import Return
import csv
from pathlib import Path

profit_loss_file = Path.cwd()/"csv_reports"/"Profits and Loss.csv"

profit_loss_list = []

with profit_loss_file.open(mode = "r", encoding = "UTF-8", newline = "") as profit_loss :
    readfiles = csv.reader(profit_loss)
    next(readfiles)
    for line in readfiles: 
        profit_loss_list.append(line[4])

def info() :
    info = [["Day40", "5298840"], ["Day41", "5197222"], ["Day42", "5319067"], ["Day43", "5374926"], ["Day44", "5866565"], ["Day45", "5884455"]]

info_profitloss_list = []
for info in profit_loss_list :
    info = float(info)
    info_profitloss_list.append(info)

day_40 = float(info[0][1])
day_41 = float(info[1][1])
day_42 = float(info[2][1])
day_43 = float(info[3][1])
day_44 = float(info[4][1])
day_45 = float(info[5][1])

difference1 = day_41 - day_40 
difference2 = day_43 - day_42
difference3 = day_45 - day_44

print("The profit and loss on Day 41 is lower than Day 40 by", abs(difference1))
print("The profit and loss on Day 43 is lower than Day 42 by", (difference2))
print("The profit and loss on Day 45 is lower than Day 44 by", (difference3))

#print(info_profitloss_list)


#day_40 = float(profit_loss[0][1])
#day_41 = float(profit_loss[1][1])
#day_42 = float(profit_loss[2][1])
#day_43 = float(profit_loss[3][1])
#day_44 = float(profit_loss[4][1])
#day_45 = float(profit_loss[5][1])

#difference1 = day_41 - day_40
#difference2 = day_43 - day_42
#difference3 = day_45 - day_44