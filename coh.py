
from ast import Return
import csv
from importlib.resources import path
import re


cash_on_hand = path.cwd()/"csv_reports"/"cash on hand.csv"
cash_on_hand_list = []

with cash_on_hand.open(mode = "r", encoding = "UTF-8", newline = "") as cash_on_hand :
        readfiles = csv.reader(cash_on_hand)
        next(readfiles)
        for line in readfiles: 
            cash_on_hand_list.append(line[1])

info_coh_list = []
for information in cash_on_hand_list :
    information = float(information)
    info_coh_list.append(information)
    
coh = [['Day40','4765310'],['Day41','3300148'],['Day42','3542813'],['Day43','2548561'],['Day44','3994410'],['Day45','3243713']]

