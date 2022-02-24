#These are the necessary library imports
import pandas as pd
from matplotlib import pyplot as plt
from functools import reduce
import matplotlib.ticker as mtick

timeperiod = 365

#BABA Information
BABA = pd.read_csv('C:\\Users\\LJone\\Fin510\\Stocks\\BABA.csv')
BABA.head()
BABA ["Date"] = pd.to_datetime(BABA["Date"])

#SOFI Information
SOFI = pd.read_csv('C:\\Users\\LJone\\Fin510\\Stocks\\SOFI.csv')
SOFI.head()
SOFI ["Date"] = pd.to_datetime(SOFI["Date"])

#SPY Information
SPY = pd.read_csv('C:\\Users\\LJone\\Fin510\\Stocks\\SPY.csv')
SPY.head()
SPY ["Date"] = pd.to_datetime(SPY["Date"])

#Now we merge using a list that we have created above

dfl=[BABA, SOFI, SPY]
df = df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Date'],
                                            how='outer'), dfl)

#Since we have what we need to graph, lets plot the returns calculated in xle
#Returns column = Price Today (Clse Day 2) / Price Yesterday (Clse D1) - 1

plt.plot(df["Date"],df["Returns_x"], label="BABA")
plt.plot(df["Date"],df["Returns_y"], label="SOFI")
plt.plot(df["Date"],df["Returns"], label="SPY")


#This is pretty much the design of the plot
plt.tight_layout()
plt.title("BABA, SOFI, & SPY Stock Returns", size = 20)
plt.legend() 
plt.show()
print (df_merged)