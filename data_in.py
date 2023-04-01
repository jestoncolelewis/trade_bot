import requests
import json
from keys import *

""" data needed:
        stock symbol
            what symbols to follow?
                reddit & twitter?
                top 50 companies?
        history - daily? weekly? monthly? yearly?
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

    r_to_buy = []
    r_to_sell = []

    for post in posts:
        if post['sentiment'] == 'Bullish' and post['sentiment_score'] >= 0.001:
            r_to_buy.append({
                'symbol': '{}'.format(post['ticker']),
                'sentiment_score': '{}'.format(post['sentiment_score'])
                })
        if post['sentiment'] == 'Bearish' and post['sentiment_score'] <= 0.000:
            r_to_sell.append({
                'symbol': '{}'.format(post['ticker']),
                'sentiment_score': '{}'.format(post['sentiment_score'])
            })

    return r_to_buy, r_to_sell

# alpha vantage
def alpha():
    func = 'TIME_SERIES_INTRADAY'
    symbol = 'AAPL'
    inv = '5min'

    a_url = 'https://www.alphavantage.co/query?function={}&symbol={}&interval={}&apikey={}'.format(func, symbol, inv, av_k)

    av_response = requests.get(a_url)
    av_data = av_response.text
    av_data = json.loads(av_data)

    return av_data

# twitter
