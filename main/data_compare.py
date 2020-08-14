from matplotlib import pyplot as plt
import seaborn as sns
import tushare as ts
import pandas as pd

def data_compare():

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

    #柱状图
    mean_share_list = [sz1['close'].mean(), sz2['close'].mean(), sz4['close'].mean(), sz5['close'].mean(), sz6['close'].mean()]
    mean_share_series = pd.Series(mean_share_list, index=['000001', '000002', '000004', '000005', '000006'])
    mean_share_series.plot(kind='bar')
    plt.xticks(rotation=360) 
    plt.show()

    #箱型图
    closedf = pd.DataFrame()
    closedf = pd.concat([closedf, sz1['close'], sz2['close'], sz4['close'], sz5['close'], sz6['close']], axis=1)  # 横向拼接数据(axis=1)
    closedf.columns = ['000001', '000002', '000004', '000005', '000006']
    closedf.plot(kind='box')
    plt.show()
