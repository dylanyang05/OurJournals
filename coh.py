
import csv
from difflib import Differ
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
            reader = csv.reader(path)
            next(reader)
    for lines in reader:
        print(lines)

coh = [['Day40','4765310'],['Day41','3300148'],['Day42','3542813'],['Day43','2548561'],['Day44','3994410'],['Day45','3243713']]

print((coh[0][1]))

