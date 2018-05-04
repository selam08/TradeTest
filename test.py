import urllib.request
import json
import pandas as pd

'''def getCoins():
    coin = open("coins.txt", "r").read()
    coins = coin.split("\n")
    for c in coins:
            if(c != ""):
              print(c + ": " + getRate(c))'''


def getRate(coin):
    r = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/" + coin)
    d = json.load(r)
    data = d[0]
    return(data['price_usd'])

def getTicket(coin):
    r = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/" + coin)
    data = json.load(r)
    return data

def getTicket2Df(coin=''):
    data = pd.read_json("https://api.coinmarketcap.com/v1/ticker/" + coin)
    return data

dataBTC = getTicket2Df()
print(dataBTC)
