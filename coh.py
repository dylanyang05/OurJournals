
import csv
from re import search
import re


print("hello")
print("I have no idea")
def read_csv(output_path,lines):
    with open(output_path,"w", newline="") as f:
        reader = csv.reader
def coh ():
    path = path.cwd()/"OURJOURNALS"/"cash_on_hand.csv"
    home = path.home()
    file_path = home/"OURJOURNALS"
    cash_on_hand = path.glob("*.txt")
    print(cash_on_hand)

    lines = []
    for cash in cash_on_hand:
        with open(cash) as f:
            text = f.read()
            lines.append(search(text))

        read_csv(path/"cash_on_hand.csv",lines) 

        cash_on_hand = re.search(r"cash on hand")
        input (f"the difference in day 40 to 41 is")
