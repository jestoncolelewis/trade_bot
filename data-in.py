import requests
import json

url = 'https://tradestie.com/api/v1/apps/reddit'

response = requests.get(url)
posts = json.loads(response.text)

to_buy = []
to_sell = []

for post in posts:
    if post['sentiment'] == 'Bullish':
        to_buy.append({
            'symbol': '{}'.format(post['ticker']),
            })
    if post['sentiment'] == 'Bearish':
        to_sell.append({
            'symbol': '{}'.format(post['ticker']),
        })
