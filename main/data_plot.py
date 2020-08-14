
import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns


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