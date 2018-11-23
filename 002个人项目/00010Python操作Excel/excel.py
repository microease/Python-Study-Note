# coding=utf-8

import numpy as np
import pandas as pd

excel_path = '2016-04-20.xls'
data = pd.read_excel(excel_path, sheetname=None)
sheet1 = data['搜索词']
df = df.drop('站点名称',axis = 0)