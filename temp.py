# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
#用字典创建数据框
dict = {'key1':['a', 'a', 'b', 'b', 'a'],
        'key2':['one','two','one','two','one'],
        'data1':np.random.randn(5),
        'data2':np.random.randn(5),
        'date':['2014-01-01 07:21:51', '2014-01-03 11:29:02', '2014-05-29 14:08:43', '2014-07-16 09:32:03', '2014-08-24 11:37:53']}

df = pd.DataFrame(dict)
df = pd.DataFrame(dict,columns=['key1','key2','data1','data2','date'])
print(df)
#对单列进行分组
mean1 = df.groupby('key1').mean()
mean2 = df.groupby('key1')['data1'].mean()#Series
mean3 = df.groupby('key1')[['data1']].mean()#DataFrame
'''print('mean1->\n',mean1)
print('mean2->\n',mean2)
print('mean3->\n',mean3)'''
#对多列进行分组
mean4 = df.groupby(['key1','key2']).mean()
mean5 = df.groupby(['key1','key2'])['data1'].mean()#Series
mean6 = df.groupby(['key1','key2'])[['data1']].mean()#DataFrame
print('mean4->\n',mean4)
print('mean5->\n',mean5)
print('mean6->\n',mean6)
mean7 = df.groupby(['key1','key2'])['data1','data2'].mean()#Series
print('mean7->\n',mean7)

