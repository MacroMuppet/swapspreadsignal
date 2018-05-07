#import pandas_datareader.data as web
import pandas_datareader as pdr
import matplotlib.pyplot as plt 
import pandas as pd
import datetime
#GS PandasDataReadTest
#gs10 = pdr.get_data_fred('GS10')
#gs10.head()

start = datetime.datetime(2013, 1, 1)

end = datetime.datetime(2018, 4, 30)


#Below is to get GDP from FRED Data with above SSTART and END Dates Manually inputted
#gdp = pdr.DataReader('GDP', 'fred', start, end)
#gdp.ix['2013-01-01']
#print(gdp) 

fincred = pdr.DataReader('TCMDODFS','fred',start,end)

#print(fincred)

df = pd.DataFrame(fincred)
df.plot()
plt.show()

df.plot(color='pink',subplots=True)
plt.title('Financial Credit Growth YoY')
plt.xlabel('Quarters')
plt.ylabel('Net Liabilities in Trillions $')
plt.show()


# Multiple series:
#In inflation = web.DataReader(['CPIAUCSL', 'CPILFESL'], 'fred', start, end)
#inflation.head()
