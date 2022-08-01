import requests

def convert(sgd):
    key = "L9FUWF60MFPOYCI3"
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={key}"
    response = requests.get(url)

    forex = response.json()

    rate = forex['Realtime Currency Exchange Rate']['5. Exchange Rate']
    USD = float(sgd) * float(rate)
    return round(USD,2)

print(convert(100))