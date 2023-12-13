import pandas as pd
import numpy as np
# 读取两个CSV文件
df1 = pd.read_csv('datasets/flights/clean.csv')
df2 = pd.read_csv('datasets/flights/dirty.csv')
# Replace values in df2 that are different from df1 with np.nan, and save the row_index, col_index
row_index = []
col_index = []
tuple_index = []
clean_dict = {}
dirt_dict = {}
print(df1.iloc[1,6])
print(df2.iloc[1,6])
for i in range(len(df1)):
    for j in range(len(df1.columns)):
        if df1.iloc[i, j] != df2.iloc[i, j]:
            row_index.append(i)
            col_index.append(j)
            tuple_index.append((i, j))
            clean_dict[(i, j)] = df1.iloc[i, j]
            dirt_dict[(i, j)] = df2.iloc[i, j]
            df2.iloc[i, j] = np.nan
# print(tuple_index)
print(df2.iloc[1,6])
print(clean_dict)