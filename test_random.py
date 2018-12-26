# -*- coding: utf-8 -*-
from random_class import Random
import matplotlib
import matplotlib.pyplot as plt


matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号

rm=Random()
result=rm.random(num_of_rand=1000)
plt.hist(result,bins=1000,normed=0,facecolor='blue',edgecolor='black',alpha=0.7)
plt.xlabel("区间")
# 显示纵轴标签
plt.ylabel("频数/频率")
# 显示图标题
plt.title("频数/频率分布直方图")
plt.show()

    




