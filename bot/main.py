import os
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor 

## pip install python-binance==0.7.9 
## Installs appropriate python-binance version

api_key = "0S6eRCHoDIrAc35nnMoWFzbiOJOhNmdVI7rM6roV872E7BfbF9u6ZBjYMp7uLFkd"

api_secret = "McQE8un0xPY5GOtHTuBDBer7my5dFSqe5ffJ2gilKWGwEMn1SY8jE7sBQoOgBNRP"

client = Client(api_key, api_secret)

client.API_URL = 'https://testnet.binance.vision/api'

global currentPrice;




''' 3 lines below print account balance of all assets, BTC balance in account, and USD balance in account'''
#print(client.get_account())

print(client.get_asset_balance(asset='BTC'))

print(client.get_asset_balance(asset='USDT'))

buyPrice = 0

'''Code below opens a web socket and continually prints price of BTC'''
btc_price = {'error':False}

def btc_price1(msg):
    if msg['e'] != 'error':
        global currentPrice
        currentPrice = msg['c'];
     #   print(currentPrice);
      #  testFunction()
       
    else:
        btc_price['error'] = True

sm = BinanceSocketManager(client)

conn = sm.start_symbol_ticker_socket('BTCUSDT', btc_price1)
sm.start()



'''Put buy/sell logic here'''
def testFunction():
        print(currentPrice)
        #  if buyPrice == 0:
         #  sell_order = client.create_order(symbol = "BTCUSDT", side = "sell", type = "MARKET", quantity = 1)
         # if currentPrice / buyPrice * 100 >= 0.5:

'''Function below exchanges USD for BTC'''
def buyBTC():
    buy_order = client.create_order(symbol = "BTCUSDT", side = "buy", type = "MARKET", quantity = 1)

'''Function below exchanges BTC for USD'''
def sellBTC():
    sell_order = client.create_order(symbol = "BTCUSDT", side = "sell", type = "MARKET", quantity = 1)

'''Function below calculates percentage difference between two numbers'''
def percentageDifference(currentPrice, buyPrice):
    difference = (currentPrice - buyPrice) / (buyPrice) * 100
    return difference 

testVar = percentageDifference(800, 1000)
print(testVar)


  






