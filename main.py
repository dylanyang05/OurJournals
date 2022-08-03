import api, coh, overheads, profit_loss

#Defining main function which consolidates all sub functions
def main():
    #Assigning exchange rate to variable
    forex = api.convert()
    #Running convert() function to write report's first line
    api.convert()
    #Running Overheads_details() to write report
    overheads.Overheads_details(forex)
    #Running coh_function() to write report
    coh.coh_function(forex)
    #Running pl_function() to write report
    profit_loss.pl_function(forex)

#Running main function to activate autonmated program
main()