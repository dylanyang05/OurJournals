import requests

key = "L9FUWF60MFPOYCI3"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={key}"
response = requests.get(url)

forex = response.json()
print(forex)

rate = forex['Realtime Currency Exchange Rate']['5. Exchange Rate']
print(rate)