from alpaca.trading.client import TradingClient
import pandas
import functions as func
from keys import *

# Key handling
API_KEY = al_paper_ak
SECRET_KEY = al_paper_sk

# Symbols
data = pandas.read_csv('./constituents.csv')
symbols = data['Symbol'].tolist()
total = len(symbols)

prices = func.get_history(API_KEY, SECRET_KEY, symbols)
func.buy_market(API_KEY, SECRET_KEY, symbols, total)