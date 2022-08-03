
import csv
import re

def read_csv(output_path,lines):
    with open (output_path, "w", newline="" ) as file:
        reader= csv.reader

def oh ():
    path = path.cwd()/"OURJOURNALS"/"Overheads.csv"

overhead_info = [['Salary Expense', 30.88], 
                ['Internet Expense', 0.47], 
                ['Marketing Expense', 4.93],
                ['Rental Expense', 20.06],
                ['Overflow Expense-Retail', 0.84],
                ['Penalty Expense', 8.91],
                ['Depreciation Expense', 16.85],
                ['Shipping Expense', 0.54],
                ['Human Resource Expense', 16.52]]
highest_expense = overhead_info.values()
max_expense = max(highest_expense)
print ("[HIGHEST OVERHEAD] SALARY EXPENSE:"), max_expense