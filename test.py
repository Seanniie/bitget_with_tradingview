import bitget.mix.position_api as position
import bitget.mix.account_api as accounts
import bitget.mix.market_api as market
import pandas as pd
import time

start = time.time() 

userInfoList = pd.read_pickle("userInfoList.pkl")

symbol = 'SBTCSUSDT_SUMCBL'
marginCoin = 'SUSDT'
productType = 'sumcbl'

name = userInfoList['name'][1]
api_key = userInfoList['api_key'][1]
secret_key = userInfoList['secret_key'][1]
passphrase = userInfoList['passphrase'][1]

accountApi = accounts.AccountApi(api_key, secret_key, passphrase, use_server_time=True, first=False)
print("time :", time.time() - start)
marketApi = market.MarketApi(api_key, secret_key, passphrase, use_server_time=True, first=False)
#비트코인 현재가격
marketPrice = marketApi.market_price(symbol)               
currentPrice = float(marketPrice['data']['markPrice'])
print("time :", time.time() - start)
account = accountApi.accounts(productType)
myAvailable = float(account['data'][0]['available'])
#print('Current Balance : ', myAvailable,'$')
print("time :", time.time() - start)
sizePer = 0.9
leverage = 1

size = round(((myAvailable * sizePer) * leverage) / currentPrice, 3)
print("time :", time.time() - start)
