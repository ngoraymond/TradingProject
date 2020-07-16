import alpaca_trade_api as trade
import config
import time
import datetime
import tradeRedditPost

def main():
    endpoint_url = 'https://paper-api.alpaca.markets'

    api = trade.REST(key_id = config.API_KEY, secret_key = config.SECRET_KEY, 
                base_url= endpoint_url, api_version='v2')

    print(api.list_positions())

    while True:
        #when starting, close all pending programs
        pending = api.list_orders(status='open')
        for orders in pending:
            api.cancel_order(orders.id)

        #get clock
        clock = api.get_clock()
        closeTime = clock.next_close.replace(tzinfo=datetime.timezone.utc).timestamp()
        openTime = clock.openTime.replace(tzinfo=datetime.timezone.utc).timestamp()
        curTime = clock.timestamp.replace(tzinfo=datetime.timezone.utc).timestamp()
        timetoClose = closeTime - curTime

        #For starters, sell when open, buy when close

        #when close
        api.submit_order(
            symbol = 'SPY',
            qty='100',
            time_in_force='cls',
            side = 'buy',
            type = 'market'
        )

        #when open
        api.submit_order(
            symbol = 'SPY',
            qty='100',
            time_in_force='opg',
            side = 'buy',
            type = 'market'
        )
    
    

if __name__ == "__main__":
    main()