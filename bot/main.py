import os
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
from tkinter import *
from tkinter import scrolledtext

## pip install python-binance==0.7.9
## Installs appropriate python-binance version
'''All Prices currently set to 0 '''
currentPrice = 0
buyPrice = 0
sellPrice = 0

<<<<<<< HEAD
buyThreshold = -0.02 
sellThreshold = 0.02
stopLoss = -0.05
=======
buyThreshold = 0.0002
sellThreshold = 0.0002
stopLoss = -0.0005
>>>>>>> 2108b84342a89d27dccee70ce08036563be53ad1
roundDecimal = 0

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
btcBalance1 = round(float(btcBalance['free']), 6)


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
        #tradeLogic()
        #sellBTC()
    else:
        btc_price['error'] = True

'''Function below exchanges USD for BTC'''
def buyBTC():
    usdBalanceBuy = client.get_asset_balance(asset='USDT')
    usdBalanceBuy1 = float(usdBalance['free'])
    decimal = (usdBalanceBuy1 / float(currentPrice)) * .95
    roundDecimal = round(decimal, 6)
    print(roundDecimal)
    buy_order = client.create_order(symbol = "BTCUSDT", side = "buy", type = "MARKET", quantity = roundDecimal)
    print('BTC Bought')
    global btcBalance1
    btcBalance1 = round(float(btcBalance['free']), 2)
   # print(str(btcBalance1) + '---')

'''Function below exchanges BTC for USD'''
def sellBTC():
    print("tryna sell")
    btcBalance2 = round(float(btcBalance['free']) * .95, 5)
    print(btcBalance2)
    sell_order = client.create_order(symbol = "BTCUSDT", side = "sell", type = "MARKET", quantity = btcBalance2)
    print("BTC Sold")

'''Function below calculates percentage difference between two numbers'''
def percentageDifference(currentPrice, buyPrice):
    if buyPrice != 0:
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
        if buyPrice != 0:
            pDifferenceSell = percentageDifference(currentPrice, buyPrice)
            print(currentPrice)
            print(buyPrice)
            
            if sellPrice != 0:
                pDifferenceBuy = percentageDifference(currentPrice, sellPrice)
                print(pDifferenceBuy)

        print(currentPrice)
        if lastOpSell == True:
            print("Buy running")
            if  buyPrice == 0:
                buyBTC()
                buyPrice = float(currentPrice)
                lastOpSell = False
<<<<<<< HEAD
                orders.insert(INSERT, " BTC Purchased for " + str(buyPrice) + "\n")    
            elif pDifferenceBuy <= buyThreshold: 
=======
                orders.insert(INSERT, " BTC Purchased for " + str(buyPrice) + "\n")
            elif pDifferenceBuy >= buyThreshold:
>>>>>>> 2108b84342a89d27dccee70ce08036563be53ad1
                buyBTC()
                buyPrice = float(currentPrice)
                lastOpSell = False
                orders.insert(INSERT, "1 BTC Purchased for " + str(buyPrice) + "\n")
        else:
            print("sell running")
          #  print(pDifferenceSell)
           # print(pDifferenceBuy)
            print(currentPrice)
            print(buyPrice)
            if pDifferenceSell >= sellThreshold:
                sellBTC()
                sellPrice = float(currentPrice)
                lastOpSell = True
                orders.insert(INSERT, "1 BTC Sold for " + str(sellPrice) + "\n")
            elif pDifferenceSell <= stopLoss:
                sellBTC()
                sellPrice = float(currentPrice)
                lastOpSell = True
                orders.insert(INSERT, "1 BTC Sold for " + str(sellPrice)+"\n")

def main():
    window.title("StockUp")
    window.geometry('400x270')
<<<<<<< HEAD
    priceTicker.grid(column=0, row=1)
    orders.grid(column=1, row=1)

    label = Label(window, text='BTC Price')
    label.grid(column=0, row=0)

    label2 = Label(window, text='Trade Log')
    label2.grid(column=1, row=0)

    labelUSD = Label(window, text = "USD Balance: " )
    labelUSD.grid(column = 0, row = 2)
    usdBal = Text(window, height = 1, width = 25)
    usdBal.grid(column=1, row = 2)
    usdBal.insert(INSERT, usdBalance1)

    
    labelBTC = Label(window, text = "BTC Balance: " )
    labelBTC.grid(column = 0, row = 3)
    btcBal = Text(window, height = 1, width = 25)
    btcBal.grid(column=1, row = 3)
    btcBal.insert(INSERT, btcBalance1)
=======
    priceTicker.grid(column=0, row=0)
    orders.grid(column=1, row=0)
>>>>>>> 2108b84342a89d27dccee70ce08036563be53ad1

    sm = BinanceSocketManager(client)
    conn = sm.start_symbol_ticker_socket('BTCUSDT', btc_price1)
    sm.start()

    window.mainloop()



if __name__ == "__main__":
     main()
