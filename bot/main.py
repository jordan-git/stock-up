import os

from binance import Client, BinanceSocketManager

# from twisted.internet import reactor 

## pip install python-binance==0.7.9 
## Installs appropriate python-binance version

api_key = "0S6eRCHoDIrAc35nnMoWFzbiOJOhNmdVI7rM6roV872E7BfbF9u6ZBjYMp7uLFkd"

api_secret = "McQE8un0xPY5GOtHTuBDBer7my5dFSqe5ffJ2gilKWGwEMn1SY8jE7sBQoOgBNRP"

client = Client(api_key, api_secret)

client.API_URL = 'https://testnet.binance.vision/api'

'''code below sells BTC for USD'''
#sell_order = client.create_order(symbol = "BTCUSDT", side = "buy", type = "MARKET", quantity = 1)

''' 3 lines below print account balance of all assets, BTC balance in account, and USD balance in account'''
#print(client.get_account())

#print(client.get_asset_balance(asset='BTC'))

#print(client.get_asset_balance(asset='USDT'))


'''Code below opens a web socket and continually prints price of BTC'''
btc_price = {'error':False}

def btc_price1(msg):
    if msg['e'] != 'error':
        print(msg['c'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
    else:
        btc_price['error'] = True

sm = BinanceSocketManager(client)

conn = sm.start_symbol_ticker_socket('BTCUSDT', btc_price1)
sm.start()




