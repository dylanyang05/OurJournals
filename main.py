import api, cash_on_hands, overheads, profit_loss

def main():
    forex = api.convert()
    overheads.overhead_function(forex)
    cash_on_hands.coh_function(forex)
    profit_loss.pl_function(forex)

main()

print(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = {rate}")
print(f"[HIGHEST OVERHEADS] {} = {}")
print(f"[CASH DEFICIT] DAY: {}, AMOUNT: {}")
print(f"[PROFIT DEFICIT] DAY: {}, AMOUNT: {}")