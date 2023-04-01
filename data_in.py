import requests
import json
from keys import *

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
    return

# alpha vantage - replace with alpaca?
def alpha(data):
    func = 'TIME_SERIES_INTRADAY'
    symbol = 'AAPL'
    inv = '5min'

    a_url = 'https://www.alphavantage.co/query?function={}&symbol={}&interval={}&apikey={}'.format(func, symbol, inv, av_k)

    av_response = requests.get(a_url)
    av_data = av_response.text
    av_data = json.loads(av_data)

    return av_data
