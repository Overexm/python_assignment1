from pycoingecko import CoinGeckoAPI
coinG = CoinGeckoAPI()
coins=coinG.get_coins_markets(vs_currency='usd',order='market_cap_desc')

#This is my second way of implementation

#import requests, json
#response=requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc')
#asd=response.text
#coins=json.loads(asd)