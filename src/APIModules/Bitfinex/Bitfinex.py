import bitfinex, urllib


# FRR	            float	    Flash Return Rate - average of all fixed rate funding over the last hour
# BID	            float	    Price of last highest bid
# BID_PERIOD	    int	        Bid period covered in days
# BID_SIZE	        float	    Size of the last highest bid
# ASK	            float	    Price of last lowest ask
# ASK_PERIOD	    int	        Ask period covered in days
# ASK_SIZE	        float	    Size of the last lowest ask
# DAILY_CHANGE	    float	    Amount that the last price has changed since yesterday
# DAILY_CHANGE_PERC	float	    Amount that the price has changed expressed in percentage terms
# LAST_PRICE	    float	    Price of the last trade
# VOLUME	        float	    Daily volume
# HIGH	            float	    Daily high
# LOW	            float	    Daily low



class Bitfinex:
    url = "https://api.bitfinex.com/v2/ticker/"
    obj_lst = None
    price = None
    def __init__(self, position_1, position_2="Null", btc=False):
        if (position_2 == "Null"):
            if (btc):
                base = "BTC"
            else:
                base = "USD"
        else:
            base = position_1
            position_1 = position_2
        if (base == position_1):
            return False

        import requests
        try:
            self.obj_lst = requests.get(self.url + "t" + position_1 + base).json()
            self.price = self.obj_lst[0]
            self.high = self.obj_lst[8]
            self.low = self.obj_lst[9]
            self.last = self.obj_lst[6]
        except urllib.error.HTTPError as err:
            if err.code == 404:
                print("%s not found" % self.pair)
            else:
                print(err)


