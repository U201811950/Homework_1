import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def calculate():
        
    df1 = pd.read_csv('stock_k_data.csv')
    df2 = pd.read_csv('stock_compare_data.csv')

    s1 = df1['pctChg']
    s2 = df2['pctChg']

    #计算贝塔系数

    print('贝塔系数为：',(np.cov(s1, s2))[0][1]/np.var(s2))

    #计算夏普比率
    Time = 146 # 此处使用数据仅有146天，年化时间由252天改为146
    Rate = 0.04 # 无风险收益率使用年化利率为4%的国债利率，并化为日利率。

    df1['ex_pct_close'] = df1['pctChg'] - Rate/Time
    print('夏普比率为：',(df1['ex_pct_close'].mean() * math.sqrt(Time))/df1['ex_pct_close'].std())


    # 使用的是简单收益率。
    # 使用深证成指（399300.SZ）代替市场指数。

def get_macd_data(short=0,long1=0,mid=0):
    data = pd.read_csv('stock_k_data.csv')
    if short==0:
        short=12
    if long1==0:
        long1=26
    if mid==0:
        mid=9
    data['sema']=pd.Series(data['close']).ewm(span=short).mean()
    data['lema']=pd.Series(data['close']).ewm(span=long1).mean()
    data.fillna(0,inplace=True)
    data['data_dif']=data['sema']-data['lema']
    data['data_dea']=pd.Series(data['data_dif']).ewm(span=mid).mean()
    data['data_macd']=2*(data['data_dif']-data['data_dea'])
    data.fillna(0,inplace=True)
    # 计算结束 画图
    plt.plot(data['date'], data['data_dea'])
    plt.xlabel('date')
    plt.ylabel('data_dea')
    plt.title('data_dea')
    plt.show()
    #画图 2
    plt.plot(data['date'], data['data_dif'])
    plt.xlabel('date')
    plt.ylabel('data_dif')
    plt.title('data_dif')
    plt.show()
    #画图 3
    plt.plot(data['date'], data['data_macd'])
    plt.xlabel('date')
    plt.ylabel('data_macd')
    plt.title('data_macd')
    plt.show()
    return 



get_macd_data(short=0,long1=0,mid=0)
