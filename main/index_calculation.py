import math
import pandas as pd
import numpy as np

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
