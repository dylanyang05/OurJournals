
from ast import Return
import csv
from importlib.resources import path
from re import search
import re


print("hello")
def read_csv(output_path,lines):
    with open(output_path,"w", newline="") as f:
        reader = csv.reader
def coh ():
    path = path.cwd()/"OURJOURNALS"/"cash_on_hand.csv"

    lines = []
    for cash in path:
        with cash.open(mode='r',encoding='UTF-8') as f:
            for lines in reader:
                reader = csv.reader(path)
                next(reader)
        print(lines)
coh = [['Day40','4765310'],['Day41','3300148'],['Day42','3542813'],['Day43','2548561'],['Day44','3994410'],['Day45','3243713']]
day_40 = float(coh[0][1])
day_41 = float(coh[1][1])
day_42 = float(coh[2][1])
day_43 = float(coh[3][1])
day_44 = float(coh[4][1])
day_45 = float(coh[5][1])
differnce1 = day_41 -day_40 
difference2 = day_43 - day_42
difference3 = day_45 - day_44
print("The cash on day 41 is lower than day 40 by",(differnce1))
print("The cash on day 43 is lower than day 42 by",(difference2))
print("The cash on day 45 is lower than day 44 by",(difference3))


