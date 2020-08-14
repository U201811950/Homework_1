import numpy as np

import pandas as pd

 

def save_csv_from_array(arr, csv_filename=None):

    """Save data in csv format"""

    if csv_filename == None:

        csv_filename="输出csv.csv"

    arr_df = pd.DataFrame(arr)

    arr_df.to_csv(csv_filename, float_format='%.3f', index=False, header=False)

 

def save_excel_from_array(arr, exc_filename=None):

    """Save data in excel format"""

    if exc_filename == None:

        exc_filename="输出excel.xlsx"

    arr_df = pd.DataFrame(arr)

    np_arr = np.array(arr)

    arr_r, arr_c = np_arr.shape

    arr_r_b = len(str(arr_r))

    arr_c_b = len(str(arr_c))

    list_index = []

    list_columns = []

    for ii in np.arange(arr_r):

        x_str = 'Y' + str(ii).zfill(arr_r_b)#The number of digits is not enough to automatically zero

        list_index.append(x_str)

    arr_df.index = list_index

 

    for ii in np.arange(arr_c):

        y_str = 'X' + str(ii).zfill(arr_c_b)

        list_columns.append(y_str)

    arr_df.columns = list_columns

 

    writer = pd.ExcelWriter(exc_filename)

    arr_df.to_excel(writer, 'page_1', float_format='%.8f')

    writer.save()

 

 
#预设数据
a1 = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45]

a2 = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

 

arr = []# 定义array（表格）

arr.append(a1)

arr.append(a2)

arr.append(a1)

arr.append(a2)



save_csv_from_array(arr)

save_excel_from_array(arr)