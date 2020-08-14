from matplotlib import pyplot as plt
import seaborn as sns
import tushare as ts
import pandas as pd

#9fa26209a915561b9ab89a732846f62eeedf5eae8c29d883220af796(my token)
token = '9fa26209a915561b9ab89a732846f62eeedf5eae8c29d883220af796'  
ts.set_token(token)  # 初始化
pro = ts.pro_api()

#002451摩恩电气-002024海特高新-300325德威新材-002338奥普光电-002321华英农业
df = pro.daily(ts_code='002451.SZ, 002024.SZ, 300325.SZ, 002338.SZ, 002321.SZ', start_date='20200201', end_date='20200601') 

#数据分类整理
sz1 = df[::5].set_index('trade_date')
sz2 = df[1::5].set_index('trade_date')
sz4 = df[2::5].set_index('trade_date')
sz5 = df[3::5].set_index('trade_date')
sz6 = df[4::5].set_index('trade_date')

#对比折线图
fig, ax = plt.subplots()
sz1.plot(ax=ax, y='close', label='002451')
sz2.plot(ax=ax, y='close', label='002024')
sz4.plot(ax=ax, y='close', label='300325')
sz5.plot(ax=ax, y='close', label='002338')
sz6.plot(ax=ax, y='close', label='002321')
plt.legend(loc='upper left')
plt.show()
#可以看出300325德威新材在今年初期股价有着加大的下跌，三月份至六月份股价平稳运行；其他四只股票在一月初期到六月末股价同样运行平稳，同时伴有小幅震荡。

#柱状图
mean_share_list = [sz1['close'].mean(), sz2['close'].mean(), sz4['close'].mean(), sz5['close'].mean(), sz6['close'].mean()]
mean_share_series = pd.Series(mean_share_list, index=['002451', '002024', '300325', '002338', '002321'])
mean_share_series.plot(kind='bar')
plt.xticks(rotation=360) 
plt.show()
#通过柱状图与折线图综合分析，德威新材的股价特点为单股价值高且年初下跌过猛，分析为受疫情影响较大，相应的，持有该股票的股民在年初亏损严重。

#箱型图
closedf = pd.DataFrame()
closedf = pd.concat([closedf, sz1['close'], sz2['close'], sz4['close'], sz5['close'], sz6['close']], axis=1)  # 横向拼接数据(axis=1)
closedf.columns = ['002451', '002024', '300325', '002338', '002321']
closedf.plot(kind='box')
plt.show()
#由箱型图可知德威新材的异常点较多，分析其经营不善或企业遭遇各种因素的变故，相比之下摩恩电气运行平稳，分析企业面对市场的消极因素应对得力。