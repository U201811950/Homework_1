import baostock as bs
import pandas as pd
import tushare as ts
from matplotlib import pyplot as plt
import seaborn as sns

import data_plot
import index_calculation
import data_processing
import exploratory_analysis


# 获取数据
data_processing.get_data_d("sz.002739")

# 画图
data_plot.plot_pic()

# 比较
exploratory_analysis.exploratory_analysis()

# 计算指数
index_calculation.calculate()