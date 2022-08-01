from pathlib import Path
import api, cash_on_hands, overheads, profit_loss

def main():
    forex = api.convert()
    overheads.overhead_function(forex)
    cash_on_hands.coh_function(forex)
    profit_loss.pl_function(forex)

main()

fp = Path.cwd()/"summary_report.txt"
with fp.open(mode='w',encoding='UTF-8') as file:
    file.write("[REAL TIME CURRENCY CONVERSION RATE] USD1 = {rate}\n[HIGHEST OVERHEADS] {} = {}\n[CASH DEFICIT] DAY: {}, AMOUNT: {}\n,[PROFIT DEFICIT] DAY: {}, AMOUNT: {}")