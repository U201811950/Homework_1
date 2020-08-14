import pandas as pd
df = pd.read_csv('sh.000016.csv')
# 导入上证50股票从2020年1月1日到2020年8月10日的日盘交易数据
from matplotlib import pyplot as plt
import seaborn as sns

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
# 从这个图中，我们可以看到两个变量之间的关系大致符合一次函数，可以得出初步的结论：单日的成交量越大，总的交易额也会随之增加