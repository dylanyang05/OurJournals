
from ast import Return
import csv
from importlib.resources import path
import re


cash_on_hand = path.cwd()/"csv_reports"/"cash on hand.csv"

cash_on_hand_list = []
coh_info =[]

with cash_on_hand.open(mode = "r", encoding = "UTF-8", newline = "") as cash_on_hand :
        readfiles = csv.reader(cash_on_hand)
        next(readfiles)
        for line in readfiles: 
            cash_on_hand_list.append(line)
            coh_info.append(float(line[2]))
print(cash_on_hand_list)
print(coh_info)

for amount in cash_on_hand_list:
      
coh = [['Day40','4765310'],['Day41','3300148'],['Day42','3542813'],['Day43','2548561'],['Day44','3994410'],['Day45','3243713']]
