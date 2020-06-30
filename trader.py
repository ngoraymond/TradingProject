import alpaca_trade_api as trade
import config

endpoint_url = 'https://paper-api.alpaca.markets'

api = trade.REST(key_id = config.API_KEY, secret_key = config.SECRET_KEY, 
            base_url= 'https://paper-api.alpaca.markets', api_version='v2')

print(api.list_positions())


api.submit_order(
    symbol = 'SPY',
    qty = '100',
    time_in_force = 'opg',
    side = 'buy',
    type = 'market'
)