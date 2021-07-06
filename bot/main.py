import os
from binance.client import Client
from binance.websockets import BinanceSocketManager
<<<<<<< HEAD
from twisted.internet import reactor 
from tkinter import *
from tkinter import scrolledtext
=======
from twisted.internet import reactor
>>>>>>> fe3802b47c29738999e370111874ae65cbf17d45

## pip install python-binance==0.7.9
## Installs appropriate python-binance version

currentPrice = 0
buyPrice = 0

window = Tk()
text =  scrolledtext.ScrolledText(window, width=40, height = 10)

api_key = "0S6eRCHoDIrAc35nnMoWFzbiOJOhNmdVI7rM6roV872E7BfbF9u6ZBjYMp7uLFkd"
api_secret = "McQE8un0xPY5GOtHTuBDBer7my5dFSqe5ffJ2gilKWGwEMn1SY8jE7sBQoOgBNRP"
client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'


''' 3 lines below print account balance of all assets, BTC balance in account, and USD balance in account'''
#print(client.get_account())
#print(client.get_asset_balance(asset='BTC'))
#print(client.get_asset_balance(asset='USDT'))


'''Code below opens a web socket and continually prints price of BTC'''
btc_price = {'error':False}

def btc_price1(msg):
    if msg['e'] != 'error':
        global currentPrice
        currentPrice = msg['c'];
<<<<<<< HEAD
        text.grid(column=0, row=0)
        text.insert(INSERT, currentPrice + "\n")       
=======
     #   print(currentPrice);
      #  testFunction()

>>>>>>> fe3802b47c29738999e370111874ae65cbf17d45
    else:
        btc_price['error'] = True

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

'''Put buy/sell logic here'''
def testFunction():
        global buyPrice
        pDifference = percentageDifference(currentPrice, buyPrice)
        print(currentPrice)
        if  buyPrice == 0:
            buyBTC()
            buyPrice = currentPrice
        elif pDifference >= .02 & buyPrice != 0:
            sellBTC()
        elif pDifference <= -0.05 & buyPrice != 0:
            sellBTC()

<<<<<<< HEAD
def main():
    print("Hello World")
    window.title("StockUp")
    window.geometry('400x270')

    sm = BinanceSocketManager(client)
    conn = sm.start_symbol_ticker_socket('BTCUSDT', btc_price1)
    sm.start()

    window.mainloop()



if __name__ == "__main__":
     main()










  






=======
            
>>>>>>> fe3802b47c29738999e370111874ae65cbf17d45
