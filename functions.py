from alpaca.data import StockHistoricalDataClient, StockLatestQuoteRequest
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

# multi symbol request - single symbol is similar
def get_history(ak, sk, *args):
    client = StockHistoricalDataClient(ak,  sk)
    multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=[*args])

    latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)

    for arg in args:
        latest_ask_price = latest_multisymbol_quotes[arg].ask_price
        print('{} - ${}' .format(arg, latest_ask_price))

def buy_market(ak, sk, *args):
    for arg in args:
        trading_client = TradingClient(ak, sk, paper=True)
        market_order_data = MarketOrderRequest(
                        symbol=arg,
                        qty=0.023,
                        side=OrderSide.BUY,
                        time_in_force=TimeInForce.DAY
                        )

        # Market order
        market_order = trading_client.submit_order(
                        order_data=market_order_data
                    )
