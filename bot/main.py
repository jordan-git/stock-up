import os
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor 
from tkinter import *
from tkinter import scrolledtext

## pip install python-binance==0.7.9
## Installs appropriate python-binance version

currentPrice = 0
buyPrice = 0
sellPrice = 0

buyThreshold = 0.02 
sellThreshold = 0.02
stopLoss = -0.05

lastOpSell = True


window = Tk()
priceTicker =  scrolledtext.ScrolledText(window, width=40, height = 10)
orders = scrolledtext.ScrolledText(window, width=40, height = 10)

api_key = "0S6eRCHoDIrAc35nnMoWFzbiOJOhNmdVI7rM6roV872E7BfbF9u6ZBjYMp7uLFkd"
api_secret = "McQE8un0xPY5GOtHTuBDBer7my5dFSqe5ffJ2gilKWGwEMn1SY8jE7sBQoOgBNRP"
client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'

usdBalance = client.get_asset_balance(asset='USDT')
btcBalance = client.get_asset_balance(asset = 'BTC')

usdBalance1 = float(usdBalance['free'])


''' 3 lines below print account balance of all assets, BTC balance in account, and USD balance in account'''
#print(client.get_account())
print(client.get_asset_balance(asset='BTC'))
print(client.get_asset_balance(asset='USDT'))


'''Code below opens a web socket and continually prints price of BTC'''
btc_price = {'error':False}

def btc_price1(msg):
    if msg['e'] != 'error':
        global currentPrice
        currentPrice = msg['c']
        priceTicker.insert(INSERT, currentPrice + "\n")
        tradeLogic() 
        #sellBTC()    
    else:
        btc_price['error'] = True

'''Function below exchanges USD for BTC'''
def buyBTC():
    decimal = (usdBalance1 / float(currentPrice)) * .90
    roundDecimal = round(decimal, 4)
    print(roundDecimal) 
    buy_order = client.create_order(symbol = "BTCUSDT", side = "buy", type = "MARKET", quantity = roundDecimal)
    

'''Function below exchanges BTC for USD'''
def sellBTC():
    sell_order = client.create_order(symbol = "BTCUSDT", side = "sell", type = "MARKET", quantity = 1)

'''Function below calculates percentage difference between two numbers'''
def percentageDifference(currentPrice, buyPrice):
    if currentPrice == 0:
        currentPriceFloat = float(currentPrice)
        difference = (currentPriceFloat - buyPrice) / (buyPrice) * 100
    else:
        difference = 0 

        return difference

    '''Put buy/sell logic here'''
def tradeLogic():
        global buyPrice
        global sellPrice
        global lastOpSell
        pDifferenceSell = percentageDifference(currentPrice, buyPrice)
        pDifferenceBuy = percentageDifference(currentPrice, sellPrice)
        print(currentPrice)
        if lastOpSell == True:
            if  buyPrice == 0:
                buyBTC()
                buyPrice = float(currentPrice)
                lastOpSell = False
                orders.insert(INSERT, "1 BTC Purchased for " + buyPrice)    
            elif pDifferenceBuy >= buyThreshold: 
                buyBTC()
                buyPrice = float(currentPrice)
                lastOpSell = False
                orders.insert(INSERT, "1 BTC Purchased for " + buyPrice)    
        else:
            if pDifferenceSell >= sellThreshold & buyPrice != 0:
                sellBTC()
                sellPrice = float(currentPrice)
                lastOpSell = True
                orders.insert(INSERT, "1 BTC Sold for " + sellPrice)    
            elif pDifferenceSell <= stopLoss & buyPrice != 0:
                sellBTC()
                sellPrice = float(currentPrice)
                lastOpSell = True
                orders.insert(INSERT, "1 BTC Sold for " + sellPrice)  

def main():
    window.title("StockUp")
    window.geometry('400x270')
    priceTicker.grid(column=0, row=0)
    orders.grid(column=1, row=0)
    
    sm = BinanceSocketManager(client)
    conn = sm.start_symbol_ticker_socket('BTCUSDT', btc_price1)
    sm.start()

    window.mainloop()



if __name__ == "__main__":
     main()










  






