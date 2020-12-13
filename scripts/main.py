from stockPrices import getStockPrice
from announcer import announce

stocks = {
	"tesla": "tsla",
	"apple": "aapl",
	"microsoft": "msft"
}

for stock in stocks:
	stockName = stock
	stockPrice = getStockPrice(stocks[stock])
	announce(stockName, stockPrice)