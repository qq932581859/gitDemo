# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sales.xlsx")
#print(df)
grouped = df.groupby('name')

'''var = df.groupby('name').agg({'ext price':'sum','quantity':'count'})
print(type(var))
print(var)'''

top10 = (df.groupby('name').agg({'ext price':'sum','quantity':'count'})
        .sort_values(by='ext price',ascending=False))[:10] .reset_index()

#print('top10->\n',top10)

#修改列名
top10.rename(columns = {'name':'客户姓名','ext price':'销售额','quantity':'销售次数'},inplace=True)
top10= top10.reset_index()
print(top10)

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

top10.plot(kind='barh',x='客户姓名',y='销售额')

plt.show()


