import requests
import json

url = "https://api.twelvedata.com/price"
symbol = None
params = {
	"symbol": symbol,
	"apikey": "374a650abc0542cdaa7a306a5f12199b",
}

def getStockPrice(ticker):
	params["symbol"] = ticker
	stock = requests.get(url, params)
	return "{:.2f}".format(float(json.loads(stock.text)['price']))