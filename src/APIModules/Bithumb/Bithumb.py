import requests, urllib

class Bithumb:

    url = "https://api.bithumb.com/public/ticker/"

    def tubric(self, tub):
        tub_url = "https://www.quandl.com/api/v3/datasets/BOE/XUDLBK74"
        try:
            tub_price = requests.get(tub_url).json()
            return(float(tub) / float(tub_price['dataset']['data'][0][1]))
        except urllib.error.HTTPError as err:
            print(err)

    def __init__(self, pair):
        self.pair = pair
        try:
            self.obj_lst = requests.get(self.url+self.pair).json()
            self.price = self.tubric(self.obj_lst['data']['average_price'])
            self.high = self.tubric(self.obj_lst['data']['max_price'])
            self.low = self.tubric(self.obj_lst['data']['min_price'])
            self.last = self.tubric(self.obj_lst['data']['sell_price'])
        except urllib.error.HTTPError as err:
            if err.code == 404:
                print("%s not found" % self.pair)
            else:
                print(err)

