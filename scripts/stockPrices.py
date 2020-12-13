import requests
import json

url = "https://api.twelvedata.com/time_series"
symbol = input("Enter a stock ticker: ")
params = {
	"symbol": symbol,
	"apikey": "374a650abc0542cdaa7a306a5f12199b",
	"interval": "1min",
	"outputsize": "1"
}

stock = requests.get(url, params)

price = json.loads(stock.text)['values'][0]['close']

print(price)