import requests
from pathlib import Path

#Defining convert function for modularization
def convert():
    #Assigning personal key to variable
    key = "L9FUWF60MFPOYCI3"
    #Assigning url with key to variable
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={key}"
    #Assigning url request to variable
    response = requests.get(url)
    #Assigning response json list as variable
    forex = response.json()
    #Extracting exchange rate and assigning to list
    rate = forex['Realtime Currency Exchange Rate']['5. Exchange Rate']

    #Assigning file path to variable
    summary_path = Path.cwd()/"summary_report.txt"
    #Opening file in write mode
    with summary_path.open(mode='w',encoding='UTF-8') as summary:
        #Write report information into file
        summary.write(f"[REAL TIME CURRENCY CONVERSION RATE]: USD1 = SGD{rate}")
        #Closing file
        summary.close()

    #Return exchange rate
    return rate
