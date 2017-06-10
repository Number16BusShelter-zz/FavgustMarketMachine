import requests, urllib

class Poloniex:
    url = "https://poloniex.com/public?command=returnTicker"

    def __init__(self, position_1 = "BTC", position_2 = "Null", btc=False):
        if (position_2 == "Null"):
            if (btc):
                base = "BTC"
            else:
                base = "USDT"
        else:
            base = position_1
            position_1 = position_2


        try:
            self.obj_lst = requests.get(self.url).json()[base+'_'+position_1]

            self.bid = self.obj_lst['highestBid']
            self.ask = self.obj_lst['lowestAsk']
            self.last = self.obj_lst['last']

            self.high = self.obj_lst['high24hr']


        except KeyError:
            print(position_2 +" to "+position_1+" does not exist \n")

