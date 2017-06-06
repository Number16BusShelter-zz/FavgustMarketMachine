from apiclient import errors

class MarketData:

    cryp_list = "https://api.coinmarketcap.com/v1/ticker/?limit=20"
    obj_lst = None

    def __init__(self):
        import requests
        self.obj_lst = None
        try:
            self.obj_lst = requests.get(self.cryp_list).json()

        except errors.HttpError as err:
            print('An error occurred: %s' % err)
            print("Coin Market Camp server is down or URL is incorrect")



    def get_json(self):
        return self.obj_lst

    def get_data(self):
        str = ""
        for obj in self.obj_lst:
            str += obj['symbol'] + " : " + obj['price_usd'] + "\n" +"24 hour volume USD: " + obj['24h_volume_usd'] + "\n\n"
        return str

    def dec_to_g_row(self):
        g_fields = ["id", "symbol", "price_usd", "price_btc", "24h_volume_usd", "percent_change_24h"]
        g_row = []
        names = ["ID", "Symbol", "Price USD", "Price BTC", "24h Volume USD", "24h Percent change"]
        g_row.append(names)
        for row in self.obj_lst:
            new_row = []
            for column in g_fields:
                new_row.append(row[column])
            g_row.append(new_row)
        return g_row

#   MarketData class contains two methods "get_json" and "get_data"
#   First one returns an object containing top 6 positions
#
#
#
#
#





