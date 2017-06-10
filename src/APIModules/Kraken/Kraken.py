import requests, urllib

class Kraken:

    def tubric(self, eur_tub):
        url = "http://api.fixer.io/latest?symbols=USD,EUR"
        try:
            tub_price = requests.get(url).json()
            return (float(eur_tub) * float(tub_price['rates']['USD']))
        except urllib.error.HTTPError as err:
            print(err)

    def __init__(self, pair, btc=False):
        url = "https://api.kraken.com/0/public/Ticker?pair="
        try:
            self.obj_lst = requests.get(url+pair+"EUR").json()
            key = list(self.obj_lst['result'].keys())[0]
            if (self.obj_lst['error'].__len__() == 0 ):

                self.ask = self.tubric(self.obj_lst['result'][key]['a'][0])
                self.bid = self.tubric(self.obj_lst['result'][key]['b'][0])
                self.last = self.tubric( self.obj_lst['result'][key]['c'][0])

                self.high = self.tubric(self.obj_lst['result'][key]['h'][0])
                self.low = self.tubric(self.obj_lst['result'][key]['l'][0])
            else:
                print("Something went wrong\n Seems like there's no such pair")
        except urllib.error.HTTPError as err:
            if err.code == 404:
                print("%s not found" % self.pair)
            else:
                print(err)

