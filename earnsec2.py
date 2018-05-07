# import pandas_datareader as pdr
import matplotlib.pyplot as plt 
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

from pandas.tseries.offsets import BDay


#need Company CIK code from SEC Edgar, remember to write a code that gets CIK code from TICKER later.

Base_url=("https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+"0000019617"+
            "&type=10-Q&dateb=&owner=exclude&count=40")

page =  requests.get(Base_url)
# page.status_codepdr
page.content

soup = BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())

table_it = soup.find_all('table',class_="tableFile2")

html_content = str(table_it)

#returns a LIST of dataframes, not asingle dataframe
df = pd.read_html(html_content)


#print(df[0])
#print(df[0].iloc[:,0])
#print(df[0].iloc[:,3])

df = df[0].iloc[:,[0,3]]

df.columns = ['filing_type','filing_date']

#print(df)

df.drop(0,axis=0,inplace=True)

df = df[df.filing_type != "10-Q/A"]


Base_url2=("https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+"0000019617"+
            "&type=10-k&dateb=&owner=exclude&count=40")

page2 =  requests.get(Base_url2)
# page.status_codepdr
page2.content

soup2 = BeautifulSoup(page2.content,'html.parser')
#print(soup.prettify())


table_it2 = soup2.find_all('table',class_="tableFile2")

html_content2 = str(table_it2)

#returns a LIST of dataframes, not asingle dataframe
df2 = pd.read_html(html_content2)


#print(df[0])
#print(df[0].iloc[:,0])
#print(df[0].iloc[:,3])

df2 = df2[0].iloc[:,[0,3]]

df2.columns = ['filing_type','filing_date']
df2.drop(0,axis=0,inplace=True)
#print(df2)

joindfs = [df, df2]
df3 = pd.concat(joindfs,axis=0,ignore_index=True)

#print(df3)

df3['filing_date']=pd.to_datetime(df3.filing_date)
#df3.sort('filing_date')
df3.sort_values(by=['filing_date'],inplace=True)

filedates = list(df3['filing_date'])

spreads = pd.read_csv('C:\\users\\caada\\projects\\swapspreadsignal\\10YSS.csv',index_col='Date')
spreads.index = pd.to_datetime(spreads.index)
spreads.sort_index(inplace=True)

spreads = spreads.subtract(spreads.shift(1))

cases = {}

for d in filedates:
    window_start = d - BDay(20)
    window_end = d + BDay(20)

    if window_start not in spreads.index:
        pass
    else:
        window = pd.date_range(window_start,window_end,freq=BDay())
        window = list(window)

        values = list(spreads.loc[window,'10YYSS'])

        cases.update({d:values})

cases_df = pd.DataFrame.from_dict(cases)

cases_df.to_csv('cases_output.csv')

