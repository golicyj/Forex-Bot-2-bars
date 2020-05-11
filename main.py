import sys
import requests
import datetime
from datetime import date, timedelta
from tradecheck import check_date_to_trade
from tradecheck import from_d, to_d, dayname_t

#stop_loss = 20
#take_profit = 100
#save_deal = 10
pair = 'EUR/USD'

check_date_to_trade()

if from_d == 0:
	print(f'Today is {dayname_t}! This is not trading day, chill out!')
	sys.exit()



url = "https://fcsapi.com/api-v2/forex/history?"
response = requests.get(url, headers={'Accept':'application/json'}, params ={
		'symbol' : pair,
		'period' :'1d',
		'from' :f'{from_d}T00:00',
		'to' :f'{to_d}T12:00',
		'access_key' :'HmdW9Gmw4N9QL9aun6c90TqO6I7GVsSv7yBG46UfxMa9L5UzXJ'
	})

cur_price = response.json()
price_open_yesterday = cur_price['response'][0]['o']
price_close_yesterday = cur_price['response'][0]['c']
price_open_today = cur_price['response'][1]['o']
price_close_today = cur_price['response'][1]['c']

def check_candle_type(openp, closep):
	
	global candle_body
	openp = float(openp)
	closep = float(closep)
	candle_type = closep - openp
	if candle_type > 0:
		candle_body = 1
	else:
		candle_body = 0
	
	return candle_body


day_1 = check_candle_type(price_open_yesterday, price_close_yesterday)
day_2 = check_candle_type(price_open_today, price_close_today)


def forecast():
	
	global forecast_result
	forecast_result = day_1 + day_2
	
	if forecast_result == 1:
		print('api-pass-command')

	if forecast_result == 0:
		print('api-sell-command')

	if forecast_result == 2:
		print('api-buy-command')


forecast()

#https://api-fxtrade.oanda.com

#candle_type(price_open_yesterday, price_close_yesterday)
#forecast()


#print(yesterday_data.strftime('%y-%m-%d'))