import requests
import json
from keys import *
from alpaca.data.historical import StockHistoricalDataClient # type: ignore
from alpaca.data.requests import StockTradesRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

""" data needed:
        stock symbol
            what symbols to follow?
                reddit & twitter?
                top 50 companies?
        history - daily
            open/close
            profit/loss in comparison with price
        opnions - reddit/twitter/other
            quantifying sentiment score from a variety of sources
"""

# reddit
def reddit():
    r_url = 'https://tradestie.com/api/v1/apps/reddit'

    response = requests.get(r_url)
    posts = json.loads(response.text)

    r_data = []

    for post in posts:
        r_data.append({
            'symbol': '{}'.format(post['ticker']),
            'sentiment': '{}'.format(post['sentiment_score'])
            })

    return r_data

# twitter
def twitter():
    t_data = []
    return t_data

# alpaca
def history(data):
    stock_client = StockHistoricalDataClient(al_paper_ak,  al_paper_sk)
    history = []
    for d in data:
        try:
            request_params = StockTradesRequest(
                symbol_or_symbols=d,
                start=datetime(2022,12,29),
                end=datetime(2022,12,31),
                limit=1
                ) # type: ignore
            
            history.append(stock_client.get_stock_trades(request_params))
        except AttributeError as err:
            print(err)
        except KeyError as err:
            print(err)

    return history
