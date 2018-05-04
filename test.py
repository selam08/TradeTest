import urllib.request
import json

def getCoins():
        coin = open("coins.txt", "r").read()
        coins = coin.split("\n")
        for c in coins:
                if(c != ""):
                  print(c + ": " + getRate(c))


def getRate(coin):
        r = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/" + coin)
        d = json.load(r)
        data = d[0]
        return(data['price_usd'])

getCoins()
 
