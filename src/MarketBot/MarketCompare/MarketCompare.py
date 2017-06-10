from src.APIModules.Bitfinex import Bitfinex
from src.APIModules.Bittrex import  Bittrex
from src.APIModules.Bithumb import Bithumb
from src.APIModules.Kraken import Kraken
from src.APIModules.Poloniex import Poloniex

def results(position, btc):
    return {
    "BF" : Bitfinex.Bitfinex(position, btc = btc).price,
    "BT" : Bithumb.Bithumb(position).price,
    "BTX" :Bittrex.Bittrex(position, btc = btc).price,
    "KK" : Kraken.Kraken(position, btc = btc).ask,
    "PX" : Poloniex.Poloniex(position, btc = btc).ask,
}

def results_pair(position_1, position_2):
    return {
        "BTX": Bittrex.Bittrex(position, usdt=True).price,
        "PX": Poloniex.Poloniex(position, usdt=True).ask,
    }

results = results("ETC", False)
for result in results:
    print(result+"'s price is "+ '\033[94m'+ str(results[result]) + '\033[0m')