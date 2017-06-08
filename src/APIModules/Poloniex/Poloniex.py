import requests, urllib

class Poloniex:
    url = "https://poloniex.com/public?command=returnTicker"

    def __init__(self, position_1 = "USDT", position_2 = "BTC"):
        try:
            self.obj_lst = requests.get(self.url).json()[position_1+'_'+position_2]

            self.bid = self.obj_lst['highestBid']
            self.ask = self.obj_lst['lowestAsk']
            self.last = self.obj_lst['last']

            self.high = self.obj_lst['high24hr']


        except KeyError:
            print(position_2 +" to "+position_1+" does not exist \n")

