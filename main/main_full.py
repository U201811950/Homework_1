import baostock as bs
import pandas as pd
import tushare as ts
from matplotlib import pyplot as plt
import seaborn as sns

def get_data_d(stock_name):
    ####登录系统####
    lg = bs.login()
    #显示登录返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond error_msg:'+lg.error_msg)

    #####获取股票历史K线数据####
    #详细指标参数

    rs = bs.query_history_k_data_plus(stock_name, "date,open,high,low,close,volume,amount,preclose,pctChg", start_date='2020-01-01', end_date='2020-08-10', frequency="d")
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus error_msg:'+rs.error_msg)

    ####打印结果集####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        #获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    ####结果输出到csv文件####
    result.to_csv("stock_k_data.csv", index=False)
    print(result)

    ####登出系统####
    bs.logout

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

def plot_pic():
    df = pd.read_csv('stock_k_data.csv')
    # 导入上证50股票从2020年1月1日到2020年8月10日的日盘交易数据
    # 折线图：股票走势
    plt.plot(df['date'], df['close'])
    plt.xlabel('date')
    plt.ylabel('Share Price')
    plt.title('Trend')
    plt.show()

    # 散点图：成交量和股价
    plt.scatter(df['volume'], df['close'])
    plt.xlabel('Volume')
    plt.ylabel('Share Price')
    plt.title('Volume & Share Price')
    plt.show()

    # 涨跌幅度
    daily_return = df['close'].pct_change()
    plt.plot(df['date'], daily_return)
    plt.xlabel('Time')
    plt.ylabel('Rise and Fall')
    plt.show()

    # 直方图
    plt.hist(daily_return)
    plt.show()

    # 核密度估计
    sns.kdeplot(daily_return)
    plt.show()

    # 相关系数矩阵
    correlation = df.corr()
    print(correlation)
    sns.heatmap(correlation, annot=True)
    plt.show()

    # 成交量与单日交易总额两个变量之间的线性回归关系
    sns.jointplot(df['volume'],df['amount'],kind='reg')
    plt.show()
    # 从这个图中，我们可以看到两个变量之间的关系大致符合一次函数，可以得出

def exploratory_analysis():

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


# 获取数据
get_data_d("sz.002739")

# 画图
plot_pic()

# 比较
exploratory_analysis()

# 计算指数
calculate()
get_macd_data()