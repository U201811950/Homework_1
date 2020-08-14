
# 众米大数据软件营小组作业_1

## 小组成员 

电气中英1801-杨晨  
电气中英1801-刘琦  
电气中英1801-胡长昊  
电气卓越1801-严政  

### 总体描述
  
本程序是一个用于获取单支或多支股票处理、清洗后的数据，计算少量重要参数，并利用 matplotlib 和 seaborn 绘图软件对股票进行数据可视化与探索性分析的python程序。  
  
*This program is a python program used to obtain processed and cleaned data of single or multiple stocks, calculate a small number of important parameters, and use matplotlib and seaborn drawing software to visualize and analyze the stock data.*  
  
#### 函数描述
  
**数据处理_刘琦 data_processing:**
```
这是一个关于获取数据及进行数据处理、清洗的代码，可以按照需要修改数据格式、数据类型等，导出csv文件；也可以直接引用。
```
  
**指数计算_严政 index_calculation:**
```
通过已经获取的从2020年1月1日到2020年8月10日的股票日盘交易数据，计算衡量个股或基金相对于整个股市的波动情况的贝塔系数与衡量股票或基金所获得的风险溢价的夏普比率。
```
  
**数据可视化&探索性分析_杨晨 data_plot:**
```
通过已经获取的从2020年1月1日到2020年8月10日的股票日盘交易数据，利用绘图软件 matplotlib 和 seaborn 对股票进行绘图分析.
```
  
**探索性分析_胡长昊 exploratory_analysis:**
```
利用 tushare 数据接口获取多支股票数据并对股票数据进行分类处理，利用 matplotlib 的 pyplot 绘制各支股票对比的股价折线图、均价柱状图以及箱型图。
```

### 安装     

为使程序正常运行需要**调用的库**包含：  
*The libraries that need to be called for the normal operation of the program include:*
```
import baostock
import tushare
import pandas 
import matplotlib 
import seaborn 
```  

此外，主文件夹下如下**csv文件**被用于保存数据，请保证其位置与名称正确。  
*In addition, the following csv file in the main folder is used to save data, please ensure that its location and name are correct.*
```
stock_compare_data.csv
stock_k_data.csv
```
### 用法
  
运行 main 程序即可获取对应股票信息并绘制相应图表。  
*Run the main program to get the corresponding stock information and draw the corresponding chart.*
```
分装函数功能或见相应文件夹中的Readme.md文件
```

### 联系方式
**QQ群：** *599539040*  

欢迎提出意见与拷贝文件。对于重大更改，请先打开一个问题以讨论您要更改的内容。  
*Pull requests and suggestions are both welcome. For major changes, please open an issue first to discuss what you would like to change.*

### 致谢
参考内容：
```
1. https://www.baostock.com
2. https://www.liaoxuefeng.com
3. https://blog.csdn.net/thfyshz/article/details/83443783
4. https://blog.csdn.net/qixizhuang/article/details/86263743
```
感谢以上开发者无私分享出的知识，并感谢训练营老师、助教所付出的努力。


