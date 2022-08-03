from ast import Return
import csv
from importlib.resources import path
from re import search
import re

def read_csv(output_path, lines) : 
    with open(output_path, "w", newline = "") as f : 
        reader = csv.reader

def profit_loss () : 
    path = path.cwd()/"OURJOURNALS"/"Profits and Loss.csv"

    lines = []
    for profit in path :
        with profit.open(mode = "r", encoding = "UTF-8") as f :
            for lines in reader :
                reader = csv.reader(path)
                next(reader)
        print(lines)

profit_loss = [["Day40", "5298840"], ["Day41", "5197222"], ["Day42", "5319067"], ["Day43", "5374926"], ["Day44", "5866565"], ["Day45", "5884455"]]
day_40 = float(profit_loss[0][1])
day_41 = float(profit_loss[1][1])
day_42 = float(profit_loss[2][1])
day_43 = float(profit_loss[3][1])
day_44 = float(profit_loss[4][1])
day_45 = float(profit_loss[5][1])

difference1 = day_41 - day_40
difference2 = day_43 - day_42
difference3 = day_45 - day_44

print("The profit and loss on Day 41 is lower than Day 40 by", abs(difference1))
print("The profit and loss on Day 43 is lower than Day 42 by", (difference2))
print("The profit and loss on Day 45 is lower than Day 44 by", (difference3))