import api, coh, overheads, profit_loss

def main():
    forex = api.convert()
    overheads.Overheads_details(forex)
    coh.coh_function(forex)
    profit_loss.pl_function(forex)

main()