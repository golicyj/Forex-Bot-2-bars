import sys
import requests
import datetime
from datetime import date, timedelta

#it's not stupid if it works

today_data = datetime.datetime.now()
yesterday_data = datetime.datetime.now() - timedelta(days=1)

dayname_t = today_data.strftime("%A")
dayname_y = yesterday_data.strftime("%A")


def check_date_to_trade():
	if dayname_t == 'Monday':
		global from_date
		global to_date
		global from_d
		global to_d
		from_date = datetime.datetime.now() - timedelta(days=4)
		to_date = datetime.datetime.now() - timedelta(days=2)
		from_d = from_date.strftime('%y-%m-%d')
		to_d = to_date.strftime('%y-%m-%d')
		return from_date
		return to_d
	elif dayname_t == 'Tuesday':
		from_date = datetime.datetime.now() - timedelta(days=4)
		to_date = datetime.datetime.now()
		from_d = from_date.strftime('%y-%m-%d')
		to_d = to_date.strftime('%y-%m-%d')
		return from_date
		return to_d
	elif dayname_t == 'Wednesday':
		from_date = datetime.datetime.now() - timedelta(days=2)
		to_date = datetime.datetime.now()
		from_d = from_date.strftime('%y-%m-%d')
		to_d = to_date.strftime('%y-%m-%d')
		return from_date
		return to_d
	elif dayname_t == 'Thursday':	
		from_date = datetime.datetime.now() - timedelta(days=2)
		to_date = datetime.datetime.now()
		from_d = from_date.strftime('%y-%m-%d')
		to_d = to_date.strftime('%y-%m-%d')
		return from_date
		return to_d
	elif dayname_t == 'Friday':
		from_date = datetime.datetime.now() - timedelta(days=2)
		to_date = datetime.datetime.now()
		from_d = from_date.strftime('%y-%m-%d')
		to_d = to_date.strftime('%y-%m-%d')
		return from_date
		return to_d
	elif dayname_t == 'Saturday':
		from_d = 0
		to_d = 0
		return from_d
		return to_d
		return dayname_t
	elif dayname_t == 'Sunday':
		from_d = 0
		to_d = 0
		return from_d
		return to_d
		return dayname_t
		

check_date_to_trade()