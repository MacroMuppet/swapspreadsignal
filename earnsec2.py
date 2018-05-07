# import pandas_datareader as pdr
import matplotlib.pyplot as plt 
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

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
print(df)

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
print(df3)