import csv
from pathlib import Path


filepath= Path.cwd()/"OurJournals"

Overheads_file= Path.cwd()/"OurJournals"/"Overheads.csv"

OurJournals_Overheads_list=[]

with Overheads_file.open (mode="r", encoding= "UTF-8") as Overheads:
    readfiles= csv.reader(Overheads)
    for line in readfiles:
        OurJournals_Overheads_list.append(line[1])
        
final_Overheadslist= []
for details in OurJournals_Overheads_list:
    details=float (details)
    final_Overheadslist.append(details)


def highestOverheads_details():
   
     for overheaddetails in Overheads_file:
        highestvalue= max(Overheads_file)
        if overheaddetails > highestvalue:
            highestvalue=overheaddetails
        message= (f"[HIGHEST VALUE] Salary Expense:", highestvalue)
        
        print (message)
