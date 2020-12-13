import pyttsx3

def announce(stockName, stockPrice):
	engine = pyttsx3.init()
	engine.say(stockName + " is currently at " + stockPrice)
	engine.runAndWait()