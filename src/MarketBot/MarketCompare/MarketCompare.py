from src.APIModules.Bitfinex import Bitfinex
from src.APIModules.Bittrex import  Bittrex
from src.APIModules.Bithumb import Bithumb
from src.APIModules.Kraken import Kraken
from src.APIModules.Poloniex import Poloniex

print(Bitfinex.Bitfinex("BTCUSD").price)
print(Bithumb.Bithumb("BTC").price)
print(Bittrex.Bittrex("BTC").price)
print(Kraken.Kraken("BTC").ask)
print(Poloniex.Poloniex("USDT", "BTC").ask)