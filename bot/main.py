from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
from tkinter import *
from tkinter import scrolledtext

## pip install python-binance==0.7.9
## Installs appropriate python-binance version
'''Declaring necesssary global variables'''
currentPrice = 0
buyPrice = 0
sellPrice = 0

'''Threshold variables'''
buyThreshold = -0.01 
sellThreshold = 0.01
stopLoss = -0.05
roundDecimal = 0

lastOpSell = True

'''GUI Elements'''
window = Tk()
priceTicker =  scrolledtext.ScrolledText(window, width=40, height = 10)
orders = scrolledtext.ScrolledText(window, width=40, height = 10)
btcBal = Text(window, height = 1, width = 25)
usdBal = Text(window, height = 1, width = 25)

'''API Keys'''
api_key = "0S6eRCHoDIrAc35nnMoWFzbiOJOhNmdVI7rM6roV872E7BfbF9u6ZBjYMp7uLFkd"
api_secret = "McQE8un0xPY5GOtHTuBDBer7my5dFSqe5ffJ2gilKWGwEMn1SY8jE7sBQoOgBNRP"
client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'

'''Fetching balances'''
usdBalance = client.get_asset_balance(asset='USDT')
btcBalance = client.get_asset_balance(asset = 'BTC')

'''Converting balances to float'''
usdBalance1 = float(usdBalance['free'])
btcBalance1 = round(float(btcBalance['free']), 6)

'''Creating socket manager object'''
sm = BinanceSocketManager(client)

'''Code below opens a web socket and continually prints price of BTC'''
btc_price = {'error':False}

def btc_price1(msg):
    if msg['e'] != 'error':
        global currentPrice
        currentPrice = msg['c']
        priceTicker.insert(INSERT, currentPrice + "\n")
        tradeLogic()
    else:
        btc_price['error'] = True

'''Function below exchanges USD for BTC'''
def buyBTC():
    usdBalanceBuy = client.get_asset_balance(asset='USDT')
    usdBalanceBuy1 = float(usdBalanceBuy['free'])
    decimal = (usdBalanceBuy1 / float(currentPrice)) * .95
    roundDecimal = round(decimal, 5)
    buy_order = client.create_order(symbol = "BTCUSDT", side = "buy", type = "MARKET", quantity = roundDecimal)
    global btcBalance1
    btcBalance1 = round(float(btcBalance['free']), 5)
    orders.insert(INSERT, str(roundDecimal)  + " BTC Purchased for " + str(usdBalanceBuy1 * .95) + "\n")
    btcBal.delete(1.0, END)
    btcBal.insert(INSERT, btcBalance1)

'''Function below exchanges BTC for USD'''
def sellBTC():
    global btcBalance
    btcBalance = client.get_asset_balance(asset = 'BTC')
    btcBalance2 = round(float(btcBalance['free']) * .95, 5) 
    sell_order = client.create_order(symbol = "BTCUSDT", side = "sell", type = "MARKET", quantity = btcBalance2)
    soldPrice = float(currentPrice) * btcBalance2
    orders.insert(INSERT, str(btcBalance2) + " BTC Sold for " + str(soldPrice) + "\n")

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
        
        global btcBalance
        global btcBalance1
        btcBalance = client.get_asset_balance(asset = 'BTC')
        btcBalance1 = round(float(btcBalance['free']), 5)
        btcBal.delete(1.0, END)
        btcBal.insert(INSERT, btcBalance1)

        global usdBalance1
        global usdBalance
        usdBalance = client.get_asset_balance(asset='USDT')
        usdBalance1 = round(float(usdBalance['free']), 5)
        usdBal.delete(1.0,END)
        usdBal.insert(INSERT, usdBalance1)

        if buyPrice != 0:
            pDifferenceSell = percentageDifference(currentPrice, buyPrice)
            
            if sellPrice != 0:
                pDifferenceBuy = percentageDifference(currentPrice, sellPrice)

        if lastOpSell == True:
            if  buyPrice == 0:
                buyBTC()
                buyPrice = float(currentPrice)
                lastOpSell = False
            elif pDifferenceBuy <= buyThreshold: 
                buyBTC()
                buyPrice = float(currentPrice)
                lastOpSell = False
        else:
            if pDifferenceSell >= sellThreshold:
                sellBTC()
                sellPrice = float(currentPrice)
                lastOpSell = True
            elif pDifferenceSell <= stopLoss:
                sellBTC()
                sellPrice = float(currentPrice)
                lastOpSell = True

'''Function to open web socket and start the bot'''
def startBot():
    conn = sm.start_symbol_ticker_socket('BTCUSDT', btc_price1)
    sm.start()

'''Function to close the websocket and stop the bot, sells BTC for USD'''
def stopBot():
    sm.close()
    sellBTC()

def main():
    window.title("StockUp")
    window.geometry('700x300')
    priceTicker.grid(column=0, row=1)
    orders.grid(column=1, row=1)

    label = Label(window, text='BTC Price')
    label.grid(column=0, row=0)

    label2 = Label(window, text='Trade Log')
    label2.grid(column=1, row=0)

    labelUSD = Label(window, text = "USD Balance: " )
    labelUSD.grid(column = 0, row = 2)
    usdBal.grid(column=1, row = 2)
    usdBal.insert(INSERT, usdBalance1)

    
    labelBTC = Label(window, text = "BTC Balance: " )
    labelBTC.grid(column = 0, row = 3)
    btcBal.grid(column=1, row = 3)
    btcBal.insert(INSERT, btcBalance1)

    startButton = Button(window, text ="Start", command = startBot)
    startButton.grid(column=0, row=4)

    stopButton = Button(window, text ="Stop", command = stopBot)
    stopButton.grid(column=1, row=4)

    window.mainloop()



if __name__ == "__main__":
     main()
