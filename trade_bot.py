from alpaca.trading.client import TradingClient
from keys import *

API_KEY = ak
SECRET_KEY = sk

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=False)

account = trading_client.get_account()
for property_name, value in account:
    print(f'"{property_name}": {value}')

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))