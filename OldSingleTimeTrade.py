import alpaca_trade_api as trade
import config
import time

def main():
    endpoint_url = 'https://paper-api.alpaca.markets'

    api = trade.REST(key_id = config.API_KEY, secret_key = config.SECRET_KEY, 
                base_url= endpoint_url, api_version='v2')

    print(api.list_positions())


    api.submit_order(
        symbol = 'SPY',
        qty = '100',
        time_in_force = 'opg',
        side = 'buy',
        type = 'market'
    )
    
    

if __name__ == "__main__":
    main()