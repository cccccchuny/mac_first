from numpy import int_
import pyupbit
import json
import schedule
from schedule import *
import time
import requests

# 로그인
access_key = 'mLgK2lFXQlB8BUIRrdkgujbSuTxRpyYngbPKZDgQ' 
secret_key = 'TLRBCfWek5t78Pn5zb3jDstsgLLVKhzTBsGxL7qf'
upbit = pyupbit.Upbit(access_key, secret_key)

#가격조회
pyupbit.get_tickers(fiat="KRW")   #거래가능 코인출력
ticker = "KRW-XRP" # 이더리움:ETH , 리플:XRP , 비트코인:BTC
# pyupbit.get_current_price(["KRW-BTC", "KRW-XRP"])
# print(pyupbit.get_current_price(["KRW-BTC", "KRW-XRP"]))  # 리스트 이용, 여러 코인 가격 받을수있음

# pyupbit.get_ohlcv(ticker=ticker, interval="minute1")  # 분봉 데이터
# pyupbit.get_ohlcv(ticker=ticker, interval="minute3")  # 3분봉 데이터
# pyupbit.get_ohlcv(ticker=ticker, interval="minute5") 
# pyupbit.get_ohlcv(ticker=ticker, interval="minute10") 
# pyupbit.get_ohlcv(ticker=ticker, interval="minute30") 
# pyupbit.get_ohlcv(ticker=ticker, interval="minute60") 
# pyupbit.get_ohlcv(ticker=ticker, interval="minute240") 
# pyupbit.get_ohlcv(ticker=ticker, interval="week")  # 월봉 데이터
# pyupbit.get_ohlcv(ticker=ticker, interval="month")  # 월봉 데이터
# print(pyupbit.get_ohlcv(ticker=ticker, interval="minute1"))

# 잔고조회
# print(upbit.get_balances())
# gb=upbit.get_balances()
# str_jango=gb[0]
# float_jango=float(str_jango['balance'])
# jango=int(float_jango)
# print(jango)


#매수 ( 매수시 원단위 )
#upbit.buy_market_order(ticker=ticker, price=10000) # 1만원 어치 시장가 매수
# upbit.buy_limit_order("KRW-XRP", 613, 10)     # 리플 613원 10개 지정가 매수

#매도 ( 매도시 수량단위 )
#upbit.sell_market_order(ticker=ticker, volume=0.00566) # 수량 시장가 매도
# upbit.sell_limit_order("KRW-XRP", 600, 20)    # 리플을 600원에 20개 지정가 매도.

# 주문조회
# uuid를 사용해서 특정 주문을 상세 조회할 수 있습니다. uuid를 사용하면 다른 파라미터는 무시됩니다.
# order = upbit.get_order('50e184b3-9b4f-4bb0-9c03-30318e3ff10a')
# print(order)


# 현재가 감시
# WebSocket을 이용해서 현재가, 호가, 체결에 대한 정보를 수신합니다.

# 첫 번째 파라미터에는 수신정보를 입력하며 ticker, orderbook, transaction을 사용할 수 있습니다.
# 두 번째 파라미터는 구독할 필터를 설정하며 암호화폐의 티커를 입력합니다. 현재 버전에서는 원화 시장만을 지원합니다.
# from pyupbit import WebSocketManager

# if __name__ == "__main__":
#     wm = WebSocketManager("ticker", ["KRW-BTC"])
#     for i in range(10):
#         data = wm.get()
#         print(data)
#     wm.terminate()
# 주의: 웹소켓의 multiprocessing을 위해 __name__ guard를 반드시 써줘야 합니다.







# 
# 1초에 한번씩 실행
# schedule.every(1).seconds.do(job)  

# # schedule test.
# def job():
#     test_time = datetime.datetime.now()
#     hour_minute_second = str(test_time.strftime('%H:%M:%S'))
#     send(hour_minute_second)

# # 메시지 송신
# def send(text):
#     with open("kakao_code.json","r") as fp:
#         tokens = json.load(fp)


#     url="https://kapi.kakao.com/v2/api/talk/memo/default/send"
#         # POST , HOST , Authorization
#         # url 만드는법 https://HOST + POST

#     # kapi.kakao.com/v2/api/talk/memo/default/send 

#     headers={ # "Bearer"이라는 문자열과 json에서 불러온 access_token의 value를 조합하여 인증키를 만든다.
#         "Authorization" : "Bearer " + tokens["access_token"]
#     }

#     data={
#         "template_object": json.dumps({ #template_object json데이터가 스트링형식으로 보내줘야해서 json.dump 사용
#             "object_type":"text",    # 타입 text 고정
#             "text":text,  # 보내려는 내용
#             "link":{                 # 링크는 필수사항인데 그냥 네이버로? 이거 어떤 의미인지 확인필요 난 구글로 해서 구글로 진행.
#                 "web_url":"www.google.com"
#             }
#         })
#     }

#     response = requests.post(url, headers=headers, data=data)
#     response.status_code

#     if response.json().get('result_code') == 0:
#         print('메시지를 성공적으로 보냈습니다.')
#     else:
#         print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))

# # 6시간마다 refresh
# def refresh_job():
#     refresh_start='refresh_start'
#     send(refresh_start)
#     with open("kakao_code.json","r") as fp:
#         tokens = json.load(fp)

#     with open("kakao_info.json","r") as info:
#         information = json.load(info)

#     data = {
#         'grant_type':'refresh_token',
#         'client_id':information["rest_api_key"],
#         'refresh_token':tokens["refresh_token"],
#         }

#     # 완성 url : https://kauth.kakao.com/oauth/token?grant_type=refresh_token&client_id=65cd9aba57ecc911ab784d4a1bc244ed&refresh_token=GGltKOKk28EUfq6nUY8TIkLU4TTyS8vDa6io4QopcJ8AAAF-q4anrA

#     response = requests.post(information["access_token_url"], data=data)
#     new_tokens = response.json()
#     new_access_tokens = new_tokens["access_token"]
#     tokens['access_token'] = new_access_tokens
#     if new_tokens["access_token"] :
#         refresh_succ = 'refresh_success'
#         send(refresh_succ)
#     else:
#         refresh_fail = 'refresh_failed'
#         send(refresh_fail)
#     with open("kakao_code.json","w") as fp:      
#         json.dump(tokens, fp)

# schedule.every(6).hours.do(refresh_job)

# while True:
#     schedule.run_pending()






# def jango_chk():
#     # print(upbit.get_balances())
#     gb=upbit.get_balances()
#     str_jango=gb[0]
#     float_jango=float(str_jango['balance'])
#     jango=int(float_jango)
#     # print(jango)
#     if jango > 0 :
#         return True
#     else :
#         return False

# print(int(jango_chk()))