import requests

import time
from datetime import datetime
#response = requests.post('http://127.0.0.1:8000/predictions/',json = {
#    "ticket": "AAPL",
#    "date": "2022-09-12",
#    "price": 120,
#    "diraction": "CALL"
#})

#print(response.json())



# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key


tickets = ['INTC', 'FISV',  'STX', 'MAT', 'ADBE', 'HSIC', 'FAST', 'CERN', 'AAL', 'INTU', 'AMGN', 'KHC', 'COST', 'CHKP', 'BIIB', 'ADI', 'BIDU', 'AAPL', 'ISRG', 'ILMN', 'CTXS', 'KLAC', 'ROST', 'PAYX', 'AVGO', 'LRCX', 'NLOK', 'ATVI', 'SBUX', 'SRCL', 'GILD', 'CSCO', 'ORLY', 'XRAY', 'VRTX', 'AMZN', 'BKNG', 'QCOM', 'ADSK', 'AMAT', 'NTAP', 'GRMN', 'VOD', 'PCAR', 'TCOM', 'EBAY', 'CTSH', 'SIRI', 'MSFT', 'NFLX', 'DLTR', 'AKAM', 'NVDA', 'ADP', 'BBBY', 'GOOG', 'WYNN', 'CHRW']

while True:
  stocksToDay = {}
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  #today = date.today()
  h = int(current_time.split(':')[0])
  print(h)
  #all_stocks = Stock.objects.all(date=str(datetime.date(datetime.now())))
  yearDeat = str(datetime.date(datetime.now())).split('-')
  day = int(yearDeat[2]) -1
  fullDate = yearDeat[0]+"-"+yearDeat[1]+"-"+str(day)
  if int(h) < 22 and len(stocksToDay) > 0:
    stocksToDay = {}
  if int(h) < 15 and len(stocksToDay) == 0:
    print('over 15')
    open = None
    num = 0
    for ticket in tickets:
      url = 'https://www.alphavantage.co/query?function=DEMA&symbol={}&interval=daily&time_period=10&series_type=close&apikey=Z4CT93FXJDPZHGNU'.format(ticket)
      r = requests.get(url)
      data = r.json()
      url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=Z4CT93FXJDPZHGNU'.format(ticket)
      r = requests.get(url)
      stockprice = r.json()
      for key in stockprice['Time Series (Daily)']:
        if num == 0:
          stocksToDay[ticket] = [float(stockprice['Time Series (Daily)'][key]['4. close']),float(data['Technical Analysis: DEMA'][key]['DEMA']),key,open]
        elif num == 1 or num == 2:
          stocksToDay[ticket].append(float(data['Technical Analysis: DEMA'][key]['DEMA']))
        else:
          break
        time.sleep(60)
      for key in stocksToDay:
        dema = float(stocksToDay[key][2])
        dema1 = float(stocksToDay[key][-2])
        dema2 = float(stocksToDay[key][-1])
        if dema > dema1 > dema2:
          print('buy')
        elif dema < dema1 < dema2:
            print('sell')
  time.sleep(60*60)
