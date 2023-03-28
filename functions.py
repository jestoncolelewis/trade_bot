from alpaca.data import StockHistoricalDataClient, StockLatestQuoteRequest
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

# multi symbol request - single symbol is similar
def get_history(ak, sk, symbols):
    client = StockHistoricalDataClient(ak,  sk)
    multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=symbols) # type: ignore

    latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)

    latest_prices = {}
    for symbol in symbols:
        latest_ask_price = latest_multisymbol_quotes[symbol].ask_price
        latest_ask_price = '{}'.format(latest_ask_price)
        latest_prices[symbol] = latest_ask_price
    
    return latest_prices

def buy_market(ak, sk, symbols, prices):
    trading_client = TradingClient(ak, sk, paper=True)

    account = trading_client.get_account()

    # Check if our account is restricted from trading.
    if account.trading_blocked: # type: ignore
        print('Account is currently restricted from trading.')
    # Check how much money we can use to open new positions.
    print('${} is available as buying power.'.format(account.buying_power)) # type:ignore

    # divide buying power by number of symbols to produce purchase price
    
    for sym in symbols:
        trading_client = TradingClient(ak, sk, paper=True)
        market_order_data = MarketOrderRequest(
                        symbol=sym,
                        notional=prices[sym],
                        side=OrderSide.BUY,
                        time_in_force=TimeInForce.DAY
                        )

        # Market order
        market_order = trading_client.submit_order(
                        order_data=market_order_data
                    )
