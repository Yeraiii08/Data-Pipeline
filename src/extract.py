import yfinance as yf

def Stock(ticker):
    stock = yf.Ticker(ticker)
    stock_history = stock.history(period="max")
    
    return stock_history