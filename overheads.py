import csv
from pathlib import Path


filepath= Path.cwd()/"Overheads.csv"

Overheads_file= Path.cwd()/"Overheads.csv"

OurJournals_Overheads_list=[]

with Overheads_file.open (mode="r", encoding= "UTF-8", newline='') as Overheads:
    readfiles= csv.reader(Overheads)
    for line in readfiles:
        OurJournals_Overheads_list.append(line[1])
        
final_Overheadslist= []
for information in OurJournals_Overheads_list:
    information=float (information)
    final_Overheadslist.append(information)


def highestOverheads_details():
    highestvalue= max(final_Overheadslist)
    for overheaddetails in final_Overheadslist:
        highestvalue= max(final_Overheadslist)
        if overheaddetails > highestvalue:
            highestvalue=overheaddetails
        message= (f"[HIGHEST VALUE] Salary Expense:", highestvalue)
        
        print (message)
