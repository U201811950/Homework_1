import baostock as bs
import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns

import data_plot
import calculate
import get_data_daily


# 获取数据
get_data_daily.get_data_d()

# 画图
data_plot.plot_pic()

# 计算指数
calculate.calculate()