import csv
from pathlib import Path
from unicodedata import category


Overheads_file= Path.cwd()/"csv_reports"/"Overheads.csv"

OurJournals_Overheads_list=[]
final_Overheadslist= []

with Overheads_file.open (mode="r", encoding= "UTF-8", newline='') as Overheads:
    readfiles= csv.reader(Overheads)
    next(readfiles)
    for line in readfiles:
        OurJournals_Overheads_list.append(line)
        final_Overheadslist.append(float(line[1]))

print(OurJournals_Overheads_list)        
print(final_Overheadslist)

highestvalue=max(final_Overheadslist)
for information in OurJournals_Overheads_list:
    if information[1] == str(highestvalue):
        highest_overhead=information[0]

def highestOverheads_details():
    message= (f"[HIGHEST OVERHEADS]: {highest_overhead}, AMOUNT: SGD{highestvalue}")
    print (message)
highestOverheads_details()