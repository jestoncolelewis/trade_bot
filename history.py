from alpaca.data import StockHistoricalDataClient, StockLatestQuoteRequest

# keys required
client = StockHistoricalDataClient("PKEBHMRF81CE33KXD7Y8",  "wxjQI2tbgnfRd0NNaVJpbbHJBKsW0sG4XOJzjDMd")

# multi symbol request - single symbol is similar
def get_history(*args):
    multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=[*args])

    latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)

    for arg in args:
        latest_ask_price = latest_multisymbol_quotes[arg].ask_price
        print('{} - ${}' .format(arg, latest_ask_price))