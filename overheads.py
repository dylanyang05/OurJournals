import csv
from pathlib import Path
from unicodedata import category


Overheads_file= Path.cwd()/"OurJournals"/"Overheads.csv"

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
    highestvalue=-1
    for overheaddetails in final_Overheadslist:
        if overheaddetails> highestvalue:
            highestvalue=overheaddetails
            index=(final_Overheadslist.index(highestvalue))
            message= (f"[HIGHEST OVERHEADS]", category[index],":", highestvalue)
    print (message)
