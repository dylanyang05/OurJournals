import api, coh, overheads, profit_loss

def main():
    forex = api.convert()
    overheads.overhead_function(forex)
    coh.coh_function(forex)
    profit_loss.pl_function(forex)

main()