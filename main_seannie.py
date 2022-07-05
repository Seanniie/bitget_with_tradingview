import json
import sys
import pandas as pd
import time
import bitget.mix.market_api as market
import bitget.mix.account_api as accounts
import bitget.mix.position_api as position
import bitget.mix.order_api as order
import bitget.mix.plan_api as plan
import bitget.mix.trace_api as trace
import telegram

bot = telegram.Bot(token='123:AAF3oscLU5z2rDzPFYd_oVe8eIjf7UqF-aA')

#Jun room
chat_id = -1001634448671 

#chat_id = -1001382521972 #Seannie 전용 방
#chat_id = 1624289906 #Bot room

#레버리지
leverage = 1

#자산의 몇프로 매수할건지(0.1이면 내 자산의 10%)
sizePer = 0.9

#필요 변수
symbol = 'SBTCSUSDT_SUMCBL'
marginCoin = 'SUSDT'
productType = 'sumcbl'

################################################################################################################
data = json.loads(sys.argv[1])
print(data)
# data = {"side":"longexit"}
#longentry, longexit, shortentry, shortexit
################################################################################################################

#유저 정보들 불러옴
userInfoList = pd.read_pickle("userInfoList.pkl")

###########반복문 시작################
for i in userInfoList.index:
    try:
        name = userInfoList['name'][i]
        api_key = userInfoList['api_key'][i]
        secret_key = userInfoList['secret_key'][i]
        passphrase = userInfoList['passphrase'][i]
    except:
        bot.sendMessage(chat_id = chat_id, text=name + ' 정보 호출 오류')

    #서버시간이 상이하다면 use_server_time을 true 로 하고 개발..
    try:
        orderApi = order.OrderApi(api_key, secret_key, passphrase, use_server_time=True, first=False)
        accountApi = accounts.AccountApi(api_key, secret_key, passphrase, use_server_time=True, first=False)
    except:
        bot.sendMessage(chat_id = chat_id, text=name + ' orderApi, accountApi 객체 생성 오류')

    #planApi = plan.PlanApi(api_key, secret_key, passphrase, use_server_time=True, first=False)

    if (i==0):
        try:
            marketApi = market.MarketApi(api_key, secret_key, passphrase, use_server_time=True, first=False)
            #비트코인 현재가격
            marketPrice = marketApi.market_price(symbol)                      
            currentPrice = float(marketPrice['data']['markPrice'])
            #print('Current BTCUSDT_UMCBL Price : ',currentPrice)
        except:
            bot.sendMessage(chat_id = chat_id, text=name + ' 비트코인 현재가격 호출 오류')
    else:
        pass

    # #레버리지 설정, 교차/격리 설정(crossed, fixed)
    # accountApi.margin_mode(symbol, marginCoin, 'fixed')
    # accountApi.leverage(symbol, marginCoin, leverage, 'long')
    # accountApi.leverage(symbol, marginCoin, leverage, 'short')

    #포지션 정보 불러옴
    try:
        positionApi = position.PositionApi(api_key, secret_key, passphrase, use_server_time=True, first=False)
        positioninfo = positionApi.single_position(symbol, marginCoin)
    except:
        bot.sendMessage(chat_id = chat_id, text=name + ' 포지션 정보 호출 오류')
    

    #롱,숏 현재 물량 체크
    try:
        long_qty = positioninfo['data'][0]['available']
        short_qty = positioninfo['data'][1]['available']
    except:
        bot.sendMessage(chat_id = chat_id, text=name + ' 롱, 숏 현재 물량 체크 오류')
################################################################################################################

    #주문 평단 계산
    def get_dealAvgPrice(orderId):
        try:
            openOrderDetail = orderApi.detail(symbol, orderId)
            time.sleep(0.1)
            avgprice = openOrderDetail['data']['priceAvg']
            return avgprice
        except:
            bot.sendMessage(chat_id = chat_id, text=name + ' 주문 평단 계산 오류')
    
    #내 계좌 잔고 확인 후 현재 매수 가능 수량 계산
    def get_size(productType):
        try:
            account = accountApi.accounts(productType)
            myAvailable = float(account['data'][0]['available'])
            #print('Current Balance : ', myAvailable,'$')

            size = round(((myAvailable * sizePer) * leverage) / currentPrice, 3)
            #print('can buy : ',size,'BTC')
            return size
        except:
            bot.sendMessage(chat_id = chat_id, text=name + ' 계좌 잔고 확인 오류')
################################################################################################################

    #롱진입
    if data['side'] == "longentry":
        if(float(long_qty)!=0):
            telegramMsg = name +'\n이미 보유 중인 롱 포지션이 있습니다. 요청 취소됨.'
            pass
        elif(float(short_qty)!=0):
            try:
                closeOrder = orderApi.place_order(symbol, marginCoin, size=short_qty, side='close_short', orderType='market', timeInForceValue='normal')
                closeOrderPrice = get_dealAvgPrice(closeOrder['data']['orderId'])
            except:
                telegramMsg = name + ' 롱진입 closeorder 오류'
            
            try:
                size = get_size(productType)
            except:
                telegramMsg = name + ' 롱진입 size 계산 오류'
            
            try:
                openOrder = orderApi.place_order(symbol, marginCoin, size, side='open_long', 
                    orderType='market', timeInForceValue='normal')
                time.sleep(0.1)
                openOrderPrice = get_dealAvgPrice(openOrder['data']['orderId'])
                telegramMsg = (name +'\n숏 청산 완료\n' + '숏 청산 AvgPrice : $' 
                    + str(closeOrderPrice) + '\n------------------------------\n롱 진입 완료\n' 
                    + '롱 진입 AvgPrice : $'+ str(openOrderPrice))
            except:
                telegramMsg = name + ' 롱진입 openorder 오류'
            
        else:
            
            try:
                size = get_size(productType)
            except:
                telegramMsg = name + ' 롱 진입 size 계산 오류 002'
            
            try:
                openOrder = orderApi.place_order(symbol, marginCoin, size, side='open_long', orderType='market', timeInForceValue='normal')
                time.sleep(0.1)
                openOrderPrice = get_dealAvgPrice(openOrder['data']['orderId'])
                telegramMsg = name +'\n롱 진입 완료\n' + '롱 진입 AvgPrice : $'+ str(openOrderPrice)
            except:
                telegramMsg = name + ' 롱진입 openorder 오류 002'
            
        bot.sendMessage(chat_id=chat_id, text=telegramMsg)  

    #숏 진입
    elif data['side'] == "shortentry":
        if(float(short_qty)!=0):
            telegramMsg = name +'\n이미 보유 중인 숏 포지션이 있습니다. 요청 취소됨.'
            pass
        elif(float(long_qty)!=0):
            try:
                closeOrder = orderApi.place_order(symbol, marginCoin, size=long_qty, side='close_long', orderType='market', timeInForceValue='normal')
                closeOrderPrice = get_dealAvgPrice(closeOrder['data']['orderId'])
            except:
                telegramMsg = name + ' 숏 진입 closeorder 오류'
            
            try:
                size = get_size(productType)
            except:
                telegramMsg = name + ' 숏 진입 size 계산 오류'
            
            try:
                openOrder = orderApi.place_order(symbol, marginCoin, size, side='open_short', orderType='market', timeInForceValue='normal')
                time.sleep(0.1)
                openOrderPrice = get_dealAvgPrice(openOrder['data']['orderId'])
                telegramMsg = (name +'\n롱 청산 완료\n' + '롱 청산 AvgPrice : $' + 
                    str(closeOrderPrice) + '\n------------------------------\n숏 진입 완료\n' 
                    + '숏 진입 AvgPrice : $'+ str(openOrderPrice))
            except:
                telegramMsg = name + ' 숏 진입 openorder 오류'
                
        else:
            try:
                size = get_size(productType)
            except:
                telegramMsg = name + ' 숏 진입 size 계산 오류 002'
            
            try:
                openOrder = orderApi.place_order(symbol, marginCoin, size, side='open_short', orderType='market', timeInForceValue='normal')
                time.sleep(0.1)
                openOrderPrice = get_dealAvgPrice(openOrder['data']['orderId'])
                telegramMsg = name +'\n숏 진입 완료\n' + '숏 진입 AvgPrice : $'+ str(openOrderPrice)
            except:
                telegramMsg = name + ' 숏 진입 openorder 오류 002'
                
        bot.sendMessage(chat_id=chat_id, text=telegramMsg)  

    #롱 종료
    elif data['side'] == "longexit":
        if(float(long_qty)==0):
            telegramMsg = name +'\n보유 중인 롱 포지션이 없습니다.'
            pass
        else:
            try:
                closeOrder = orderApi.place_order(symbol, marginCoin, size=long_qty, side='close_long', orderType='market', timeInForceValue='normal')    
            except:
                telegramMsg = name + ' 롱 종료 closeOrder 오류'
                
            try:
                time.sleep(0.1)
                closeOrderPrice = get_dealAvgPrice(closeOrder['data']['orderId'])
                telegramMsg = name +'\n롱 청산 완료\n' + '롱 청산 AvgPrice : $' + str(closeOrderPrice)
            except:
                telegramMsg = name + ' 롱 종료 closeOrderPrice 오류'
            
        bot.sendMessage(chat_id = chat_id, text=telegramMsg)

    #숏 종료
    elif data['side'] == "shortexit":
        if(float(short_qty)==0):
            telegramMsg = name +'\n보유 중인 숏 포지션이 없습니다.'
            pass
        else:
            try:
                closeOrder = orderApi.place_order(symbol, marginCoin, size=short_qty, side='close_short', orderType='market', timeInForceValue='normal')    
            except:
                telegramMsg = name + ' 숏 종료 closeOrder 오류'
                
            try:
                time.sleep(0.1)
                closeOrderPrice = get_dealAvgPrice(closeOrder['data']['orderId'])
                telegramMsg = name +'\n숏 청산 완료\n' + '숏 청산 AvgPrice : $' + str(closeOrderPrice)
            except:
                telegramMsg = name + ' 숏 종료 closeOrderPrice 오류'
                
        bot.sendMessage(chat_id = chat_id, text=telegramMsg)

    #bot.sendMessage(chat_id = chat_id, text=str(time.time()-start) + 's 소요')
    