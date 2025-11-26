import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 1.创建画布
# figsize:指定图的长宽, dpi:图像的清晰度, 返回fig对象
plt.figure(figsize=(10, 10), dpi=100) # 参1: 画布大小(宽, 高)   参2: dpi(像素密度)
# 2.绘制折线图
plt.plot([1, 2, 3, 4, 5, 6 ,7], [17,17,18,15,11,11,13]) # 参数1: x轴数据   参数2: y轴数据
# 3.显示图像
plt.show()

# 画出温度变化图
# 0.准备x, y坐标的数据
x = range(60) # 准备x轴(60分钟) 和 y轴(每分钟的温度) 的数据.
y_temperature = [random.uniform(15, 28) for i in x]
# 增加温度数据
y_temperature1 = [random.uniform(1, 13) for i in x]
# 1.创建画布
plt.figure(figsize=(20, 8), dpi=80)
# 2.绘制折线图
plt.plot(x, y_temperature, label="city1")
# 使用多次plot可以画多个折线
plt.plot(x, y_temperature1, color='r', linestyle='--', label="city2")

# 添加x,y轴刻度
# 构造x轴刻度标签
x_ticks_label = ["11点{}分".format(i) for i in x]
# 构造y轴刻度
y_ticks = range(40)
y_ticks_label = ["{}度".format(i) for i in range(40)]
# 修改x,y轴坐标的刻度显示
plt.xticks(x[::5], x_ticks_label[::5])
plt.yticks(y_ticks[::5], y_ticks_label[::5])

plt.grid(True, linestyle='--', alpha=0.5)  # 添加网格显示 # 参1: 网格线的样式 - / -- / -. / : 参2: 网格线的透明度
plt.xlabel("时间") # 添加描述信息
plt.ylabel("温度")
plt.title("中午11点0分到12点之间的温度变化图示", fontsize=20)
# plt.savefig("test.png")

plt.legend(loc="best")# 显示图例
plt.show() # 3.显示图像


# 多个坐标系显示— plt.subplots(面向对象的画图方法)
# 推荐subplots函数
# matplotlib.pyplot.subplots(nrows=1, ncols=1, **fig_kw) 创建一个带有多个axes(坐标系/绘图区)的图
# nrows, ncols : 设置有几行几列坐标系, Number of rows/columns of the subplot grid.
# Returns: fig : 图对象
#          axes : 返回相应数量的坐标系
# 0.准备数据
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(1, 5) for i in x]

# 1.创建画布
# plt.figure(figsize=(20, 8), dpi=100)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)

# 2.绘制图像
# plt.plot(x, y_shanghai, label="上海")
# plt.plot(x, y_beijing, color="r", linestyle="--", label="北京")
axes[0].plot(x, y_shanghai, label="上海")
axes[1].plot(x, y_beijing, color="r", linestyle="--", label="北京")

# 2.1 添加x,y轴刻度
# 构造x,y轴刻度标签
x_ticks_label = ["{}分".format(i) for i in x]
y_ticks = range(40)

# 刻度显示
# plt.xticks(x[::5], x_ticks_label[::5])
# plt.yticks(y_ticks[::5])
axes[0].set_xticks(x[::5])
axes[0].set_yticks(y_ticks[::5])
axes[0].set_xticklabels(x_ticks_label[::5])
axes[1].set_xticks(x[::5])
axes[1].set_yticks(y_ticks[::5])
axes[1].set_xticklabels(x_ticks_label[::5])

# 2.2 添加网格显示
# plt.grid(True, linestyle="--", alpha=0.5)
axes[0].grid(True, linestyle="--", alpha=0.5)
axes[1].grid(True, linestyle="--", alpha=0.5)

# 2.3 添加描述信息
# plt.xlabel("时间")
# plt.ylabel("温度")
# plt.title("中午11点--12点某城市温度变化图", fontsize=20)
axes[0].set_xlabel("时间", fontsize=12)
axes[0].set_ylabel("温度", fontsize=12)
axes[0].set_title("中午11点--12点某城市温度变化图", fontsize=20)
axes[1].set_xlabel("时间", fontsize=12)
axes[1].set_ylabel("温度", fontsize=12)
axes[1].set_title("中午11点--12点某城市温度变化图", fontsize=20)

# # 2.4 图像保存
#plt.savefig("./test.png")

# # 2.5 添加图例
# plt.legend(loc=0)
axes[0].legend(loc=0)
axes[1].legend(loc=0)

# 3.图像显示
plt.show()


# 折线图
# 0.准备数据
x = np.linspace(-10, 10, 100)
y = np.sin(x)
# 1.创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 2.绘制函数图像
plt.plot(x, y)
# 2.1 添加网格显示
plt.grid()
# 3.显示图像
plt.show()

# 柱形图
# x = np.linspace(-10, 10, 20)
# y = np.sin(x)
x = ['A', 'B', 'C', 'D']
y = [10, 6, 15, 21]
# 1.创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 2.绘制函数图像
plt.bar(x, y, color='skyblue', edgecolor='black') # 柱形图
# 2.1 添加网格显示
plt.grid()
plt.title("Simple Bar Chart")  # 设置图表标题
plt.xlabel("Categories")  # 设置X轴标签
plt.ylabel("Values")  # 设置Y轴标签
# 3.显示图像
plt.show()

# 散点图
x = np.linspace(-10, 10, 20)
y = np.sin(x)
# 1.创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 2.绘制函数图像
plt.scatter(x, y, color='skyblue', edgecolor='black') # 散点图
# 2.1 添加网格显示
plt.grid()
plt.title("Simple Scatter Plot")  # 设置图表标题
plt.xlabel("X-axis")  # 设置X轴标签
plt.ylabel("Y-axis")  # 设置Y轴标签
# 3.显示图像
plt.show()

# 直方图
data = np.random.randn(500)  # 生成500个服从标准正态分布的随机数
# 2. 创建画布
plt.figure(figsize=(10, 6))
# 3. 绘制直方图
# bins=30：将数据分成 30 个等宽的区间，每个区间的宽度相同，统计每个区间内数据的频率。
# color='blue'：设置直方图条形为蓝色。
# alpha=0.7：设置条形的透明度为 0.7，使得条形稍微透明。
# rwidth=0.85：将条形的宽度设为区间宽度的 85%，留下 15% 的间隔，以便更清晰地分辨各个条形。
plt.hist(data, bins=30, color='blue', alpha=0.7, rwidth=0.85)
# 4. 添加标题和标签
plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
# 5. 显示图像
plt.grid(True)
plt.show()

# 饼图
sizes = [25, 35, 25, 15]
labels = ['Category A', 'Category B', 'Category C', 'Category D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')  # 绘制饼图，显示百分比
plt.title("Simple Pie Chart")  # 设置图表标题
plt.show()  # 显示图表