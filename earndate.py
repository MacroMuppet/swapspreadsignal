import pandas_datareader as pdr
import matplotlib.pyplot as plt 
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

Base_url=("http://www.moneycontrol.com/company-facts/"+
            "marutisuzukiindia/board-meetings/MS24#MS24")

page =  requests.get(Base_url)
page.status_code
page.content

soup = BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())

table_it = soup.find_all('table',class_='tbldivid')
#print(table_it)

date_list=[] ; event_list=[] ;
for mytable in table_it:
    try:
        rows = mytable.find_all('tr')
        for tr in rows:
            cols = tr.find_all('td')
            for count, i in enumerate(cols):
                er = i.text 
                ee = er.encode('utf8')
                ee = str(ee,'utf-8')

                if count % 2 == 0:
                    date_list.append(ee)

                if count % 2 == 1:
                    event_list.append(ee)
    except:
        print('no thread')

#Below checks printing of the date and what event list. 
#print(date_list)
#print(event_list)

df = pd.DataFrame({'Meeting Date':date_list,'Remark':event_list})
df = df.loc[df['Remark'].isin(['Quarterly Results','Audited Results & Dividend'])]
df_5 = df.head(16)
print(df_5)
