
# 一、数据处理
by电气中英1801班 刘琦 U201811353
## 描述
这是一个关于获取数据及进行数据处理、清洗的代码，可以按照需要修改数据格式、数据类型等，导出csv文件；也可以直接引用。
## 安装
1. baostock：股票数据接口模块，通过API接口获取股票数据，如：交易日期，开盘价，收盘价，最高价，最低价，总成交量等等。
2. pandas:基于NumPy数组构建的,使数据预处理、清洗、分析工作变得更快更简单。本例中用于返回DataFrame类型。
## 用法
1. 引用baostock，pandas库。
2. 登入baostock系统后，引用query_history_k_data_plus函数，给出参数：股票代码，所需数据日期区间，读取数据类型，设定数据频率（如5min,15min,day,week,month等）。
3. 使用pandas返回DataFrame类型，获取数据后进行清洗无效数据操作，导出csv文件。
4. 登出baostock系统。
## 参考
1. https://www.baostock.com
2. https://www.liaoxuefeng.com