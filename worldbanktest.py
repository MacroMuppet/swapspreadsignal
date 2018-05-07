#from pandas_datareader import wb
#In [2]: mathces = wb.search('gdp.*capita.*const')
#Then you would use the download function to acquire the data from the World Bank’s servers:

#In [3]: dat = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX'], start=2005, end=2008)

#In [4]: print(dat)
#                      NY.GDP.PCAP.KD
#country       year
#Canada        2008  36005.5004978584
#              2007  36182.9138439757
#Mexico        2008  8113.10219480083
#              2007  8119.21298908649
#United States 2008  43069.5819857208
#              2007  43635.5852068142
#The resulting dataset is a properly formatted DataFrame with a hierarchical index, so it is easy to apply .groupby transformations to it:

#In [6]: dat['NY.GDP.PCAP.KD'].groupby(level=0).mean()
#Out[6]:
#country
#Canada           35765.569188
#Mexico            7965.245332
#United States    43112.417952
#dtype: float64
#Now imagine you want to compare GDP to the share of people with cellphone contracts around the world.

#In [7]: wb.search('cell.*%').iloc[:,:2]
#Out[7]:
#                     id                                               name
#3990  IT.CEL.SETS.FE.ZS  Mobile cellular telephone users, female (% of ...
#3991  IT.CEL.SETS.MA.ZS  Mobile cellular telephone users, male (% of po...
#4027      IT.MOB.COV.ZS  Population coverage of mobile cellular telepho...
#Notice that this second search was much faster than the first one because pandas now has a cached list of available data series.

#In [13]: ind = ['NY.GDP.PCAP.KD', 'IT.MOB.COV.ZS']
#In [14]: dat = wb.download(indicator=ind, country='all', start=2011, end=2011).dropna()
#In [15]: dat.columns = ['gdp', 'cellphone']
#In [16]: print(dat.tail())
#                        gdp  cellphone
#country   year
#Swaziland 2011  2413.952853       94.9
#Tunisia   2011  3687.340170      100.0
#Uganda    2011   405.332501      100.0
#Zambia    2011   767.911290       62.0
#Zimbabwe  2011   419.236086       72.4
#Finally, we use the statsmodels package to assess the relationship between our two variables using ordinary least squares regression. Unsurprisingly, populations in rich countries tend to use cellphones at a higher rate:

#In [17]: import numpy as np
#In [18]: import statsmodels.formula.api as smf
#In [19]: mod = smf.ols('cellphone ~ np.log(gdp)', dat).fit()
#In [20]: print(mod.summary())

from pandas_datareader import wb
import matplotlib.pyplot as plt 
import pandas as pd
import datetime
# Below searches for the indicator code to put in wb.download(indicator='XXXXXXXXX')   IE NY.GDP.PCAP.KD for gdp per capita growth
#mathces = wb.search('gdp').iloc[:,:5]
#                                                    name  \
#641                                Per capita GDP growth
#643                                      GDP (current $)
#644                                GDP growth (annual %)
#645                                GDP (constant 2005 $)
#646    GDP per capita, PPP (constant 2011 internation...
#1456                        Trade in services (% of GDP)
#print(mathces)
#dat = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX'], start=2008, end=2018)
dat = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX'], start=2008, end=2018)
#print(dat)

#BELOW ATTEMPTS TO PLOT ONE LINE OF CODE WITH MATOLLIB.PYPLOT
df = pd.DataFrame(dat)
df.unstack(level=0).plot(kind='line', subplots=True)
print(dat)
#df.plot()
#plt.show()

df.plot(color='pink',subplots=True)
plt.title('GDP Per Capita Per Copytuntry Over 10 Years')
plt.xlabel('Year')
plt.ylabel('Gdp Per Capita in US $')
#plt.show()

#dat['NY.GDP.PCAP.KD'].groupby(level=0).mean()
#cellsearch = wb.search('cell.*%').iloc[:,:5]
#print(cellsearch)
