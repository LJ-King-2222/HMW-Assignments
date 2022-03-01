#These are the necessary library imports
import pandas as pd
from matplotlib import pyplot as plt
from functools import reduce
import matplotlib.ticker as mtick
from pylab import mpl, plt

timeperiod = 365


HW1DATA = pd.read_csv('C:\\Users\\LJone\\Fin510\\Stocks\\HW1DATA.csv')
HW1DATA.head()
HW1DATA ["Date"] = pd.to_datetime(HW1DATA["Date"])

#Now we merge using a list that we have created above

dfl=[HW1DATA]
df = df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Date'],
                                            how='outer'), dfl)

#Since we have what we need to graph, lets plot the returns calculated in xle
#Stock column = Price Today (Clse Day 2) / Price Yesterday (Clse D1) - 1

plt.plot(df["Date"],df["BABA"], label="BABA")
plt.plot(df["Date"],df["BABABB"], label="BABABB")
plt.plot(df["Date"],df["SOFI"], label="SOFI")
plt.plot(df["Date"],df["SOFIBB"], label="SOFIBB")
plt.plot(df["Date"],df["SPY"], label="SPY")
plt.plot(df["Date"],df["SPYBB"], label="SPYBB")


#This is pretty much the design of the plot
plt.tight_layout()
plt.title("YF & BB Data BABA, SOFI, & SPY Stock Returns", size = 20)
plt.legend() 
plt.show()
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
%config InlineBackend.figure_format = 'svg'
print (df) 