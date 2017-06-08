import requests, urllib

class Bittrex:
    url = "https://bittrex.com/api/v1.1/public/getmarketsummary?market="

    def __init__(self, position_1 = "USDT", position_2 = "BTC"):

        print('Warning Bittrex class is only capable of comparing 2 positions or USDT with BTC/ETH!\nYou are trying to compare '+position_1+' with '+position_2+' ')
        try:
            if (position_1 == "BTC"):
                position_1 = "USDT"
            self.obj_lst = requests.get(self.url + position_1 + "-" + position_2).json()
            if (self.obj_lst['success']):

                self.ask = self.obj_lst['result'][0]['Ask']
                self.bid = self.obj_lst['result'][0]['Bid']

                self.price = self.last = self.obj_lst['result'][0]['Last']
                self.high = self.obj_lst['result'][0]['High']
                self.low = self.obj_lst['result'][0]['Low']
            else:
                print("Something went wrong\n Seems like there's no such pair")
        except urllib.error.HTTPError as err:
            if err.code == 404:
                print("%s not found" % self.pair)
            else:
                print(err)

