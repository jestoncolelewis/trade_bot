from alpaca.trading.client import TradingClient
import pandas
import functions as func
from keys import *

# Key handling
API_KEY = paper_ak
SECRET_KEY = paper_sk

# Symbols
data = pandas.read_csv('./constituents.csv')
symbols = data['Symbol'].tolist()

prices = func.get_history(API_KEY, SECRET_KEY, symbols)
func.buy_market(API_KEY, SECRET_KEY, symbols, prices)