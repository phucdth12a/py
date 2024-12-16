from vnstock3 import Vnstock
from datetime import datetime, timedelta
import pandas_ta as ta
import math
import pandas as pd


stock = Vnstock().stock(symbol='ACB', source='VCI')

result = {"1":[],"2":[]}

currentDate = datetime.today()
currentDateString = currentDate.strftime('%Y-%m-%d')
oldDate = currentDate - timedelta(days=60)
oldDateString = oldDate.strftime('%Y-%m-%d')

def getData(name):
    try:
        stockOne = Vnstock().stock(symbol=name, source='VCI')
        df = stockOne.quote.history(start=oldDateString, end=currentDateString, interval='1D')
        if (len(df)) == 43:
            macd = ta.macd(df['close'])
            i = len(macd) - 1
            old_i = i - 1
            if macd['MACDs_12_26_9'][i] < macd['MACD_12_26_9'][i] and macd['MACDs_12_26_9'][old_i] > macd['MACD_12_26_9'][old_i]:
                result['1'].append(name)
            old2_i = old_i - 1
            if macd['MACDs_12_26_9'][i] < macd['MACD_12_26_9'][i] and macd['MACDs_12_26_9'][old_i] < macd['MACD_12_26_9'][old_i] and macd['MACDs_12_26_9'][old2_i] > macd['MACD_12_26_9'][old2_i]:
               result['2'].append(name)
        # print(macd)
    except:
        print("An exception occurred == ", name)

listVN30 = stock.listing.symbols_by_group('VN30')
for i in range(len(listVN30)):
    getData(listVN30[i])


# industries = stock.listing.symbols_by_industries()
# for i in range(len(industries)):
#     getData(industries['symbol'][i])
#     print(industries['symbol'][i])

# getData('VNNDD')
# getData('VND')

print(result)
