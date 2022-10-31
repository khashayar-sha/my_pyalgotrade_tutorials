import yfinance as yf

data = yf.download("SPY", start="1999-01-01", end="2022-9-30")
data.to_csv("spy.csv")
