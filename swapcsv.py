# import pandas_datareader as pdr
import matplotlib.pyplot as plt 
import pandas as pd
import datetime
import requests
import numpy
from bs4 import BeautifulSoup

#converts local bank data ascending CSV file in swapspreadsignal folder to dataframe
data = pd.read_csv('10YSS.csv',parse_dates=True,index_col=0)
print(data.info())
data.loc[:,'10YYSS'] *= -1
#data1y = data.head(362)
#data90d = data.head(n=90)
#data30d = data.head(n=30)
#print(data1y.std())
#data.info()
#y1 = data.iloc[:260,1]
#print(y1.std())
#p90= data.iloc[:65,1]
#print(p90.std())
period = 65
#df_roll = pd.rolling_std(data,window=period)

#creates rolling std deviation and moving average period adds it to dataframe
#data.index('Date')
data.sort_index(inplace=True)
PerStDv = str(period)+'dStdDv'
data[PerStDv] = data['10YYSS'].rolling(window=period,center=False).std()
data['MovAv'] = data['10YYSS'].rolling(window=period,center=False).mean()

data['BB+'] = data['MovAv']+data[str(period)+'dStdDv']*2
data['BB-'] = data['MovAv']-data[str(period)+'dStdDv']*2

#print(data)
#data.plot()
data.plot(x=index,'10YYSS','MovAv')
#data.PerStDv.plot(secondary_y=True, style='g')
#data.plot(x='Date',y1='10YYSS',y2='MovAv')
#data.plot('Date','10YYSS')
#data.plot('Date','MovAv',linestyle='dashed')
plt.show()

#data.plot()
#plt.show()

#prints spreads chart while printing rolling std deviation for period below linear line
"""ax1 = plt.subplot(2,1,1)
data['10YYSS'].plot()
ax2 = plt.subplot(2, 1, 2, sharex = ax1)
data['90StdDv'].plot()
plt.legend(loc='best')
plt.show()"""  

#print(df_roll.iloc[period:period+1,]) #prints the std deviation ofpip the last day in Period variable. ex 65 , then 65 trailing std deviation 
# print(data.std(:365,))

#data = pd.DataFrame.from_csv('10YSS.csv')

#print(data.head(n=5)) #tests whether filled in correctly

