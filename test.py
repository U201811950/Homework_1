import pandas as pd
import numpy as np
from scipy import stats
import tushare as ts
import matplotlib.pyplot as plt

from pylab import mpl

token = '9fa26209a915561b9ab89a732846f62eeedf5eae8c29d883220af796'  
    ts.set_token(token)  # 初始化
    pro = ts.pro_api()


mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
stock='sh'
df=ts.get_k_data(stock,start='1990-12-20')
df.index=pd.to_datetime(df.date)
#del df['date'] #删掉该列
df.tail() #这时候可以看到索引已经是date了
lograte=np.log(df.close/df.close.shift(1))[1:]
month=[]
index=lograte.index
for i in range(0,np.size(lograte)):
    month.append(''.join([index[i].strftime("%Y"),index[i].strftime("%m")]))
    y=pd.DataFrame(lograte.values,month,columns=['月收益率'])
    y.tail()
ret_monthly=y.groupby(y.index).sum()
ret_monthly.tail()
stock='601318'
df = ts.get_k_data(code=stock, ktype='D', autype='qfq', start='2007-3-1')
df.index=pd.to_datetime(df['date'])
logret=np.log(df.close/df.close.shift(1))[1:]
year=[]
d0=df.index
for i in range(0,np.size(logret)):
    year.append(d0[i].strftime("%Y"))
    y=pd.DataFrame(logret.values,year,columns=['年收益率'])
    ret_annual=np.exp(y.groupby(y.index).sum())-1
    ret_annual