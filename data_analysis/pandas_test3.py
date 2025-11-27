import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 数据合并
# pd.concat实现数据合并
# pd.concat([data1, data2], axis=1) 按照行或列进行合并,axis=0为列索引，axis=1为行索引
# 按照行索引进行
wis = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data")
print(wis.shape)
wis2 = pd.concat([wis, wis], axis=0)  #axis=0为行, axis=1为列
print(wis2.shape)

# pd.merge(left, right, how='inner', on=None) # 可以指定按照两组数据的共同键值对合并或者左右各自
# left: DataFrame
# right: 另一个DataFrame
# on: 指定的共同键
# how:按照什么方式连接
# Merge method	SQL Join Name
# left	        LEFT OUTER JOIN
# right	        RIGHT OUTER JOIN
# outer	        FULL OUTER JOIN
# inner	        INNER JOIN

# 内连接
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                        'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                        'key2': ['K0', 'K0', 'K0', 'K0'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})
# 默认内连接
result = pd.merge(left, right, on=['key1', 'key2'])
# print(result)
# 左连接
result = pd.merge(left, right, how='left', on=['key1', 'key2'])
# 右连接
result = pd.merge(left, right, how='right', on=['key1', 'key2'])
# 外连接
result = pd.merge(left, right, how='outer', on=['key1', 'key2'])

# 数据分组
df = pd.read_csv('./data/uniqlo.csv')
# agg -> Aggregate(聚合的意思)
# 格式: df.groupby(['分组字段1', '分组字段2'...]).agg({'列名1':'聚合函数名', '列名2':'聚合函数名'...})

# groupby分组聚合
# df.groupby分组函数返回分组对象
# 基于一列进行分组
gs = df.groupby(['gender_group']) # 基于顾客性别分组
print(gs) #  # DataFrameGroupBy  -> DataFrame分组对象
print(gs['city'])
# 基于多列进行分组
gs2 = df.groupby(['gender_group', 'city']) # 基于顾客性别、不同城市分组
print(gs2)

# 分组后获取各个组内的数据
# 取出每组第一条或最后一条数据
gs2 = df.groupby(['gender_group', 'channel'])
# print(gs2.first()) # 取出每组第一条数据
# print(gs2.last()) # 取出每组最后一条数据

# 按分组依据获取其中一组
# print(gs2.get_group(('Female', '线上')))

# 分组 + 聚合(聚合字段只有1个) - 需求: 根据 城市 和 销售渠道分组, 计算: 销售金额.
df.groupby(['city', 'channel']).agg({'revenue':'sum'})      # 通用版(掌握) 返回DataFrame对象

# 分组 + 聚合(聚合字段有2个, 聚合操作相同) - 需求: 根据 城市 和 销售渠道分组, 计算: 销售金额, 订单数量 总和.
df.groupby(['city', 'channel']).agg({'revenue':'sum', 'order':'sum'})

# 分组 + 聚合(聚合字段有2个, 聚合操作不同) - 需求: 根据 城市 和 销售渠道分组, 分别计算: 销售金额的平均值, 成本的总和.
df.groupby(['city', 'channel']).agg({'revenue': 'mean', 'unit_cost': 'sum'})

# 分组聚合 - 分组后对多列分别使用不同的聚合函数
# df.groupby(['列名1', '列名2']).agg({
#     '指定列1':'聚合函数名',
#     '指定列2':'聚合函数名',
#     '指定列3':'聚合函数名'
# })
# 按城市和线上线下划分，分别计算销售金额的平均值、成本的总和
gs3 = df.groupby(['city', 'channel']).agg({
    'revenue':'mean',
    'unit_cost':'sum'
})
# print(gs3)

# 分组过滤操作
# df.groupby(['列名1',...]).filter(
#     lambda x: do something return True or False
# )
# 按城市分组，查询每组销售金额平均值大于200的全部数据
# gs4 = df.groupby(['city']).filter(lambda s: s['revenue'].mean() > 240)
gs4 = df.groupby(['city'])['revenue'].filter(lambda s: s.mean() > 240)
print(gs4)

df.groupby(['city']).revenue.count()
df.groupby(['city'])['revenue'].count()
df.groupby(['city']).agg({'revenue':'count'})

df_temp = df.groupby(['city'], as_index=False).agg({'revenue':'count'})
# 修改列名
df_temp.columns = ['city', 'revenue_count']
# 交叉表与透视表
# 交叉表用于计算一列数据对于另外一列数据的分组个数(用于统计分组频率的特殊透视表)
data = {
    '性别': ['男', '女', '男', '女', '男', '女', '女', '男'],
    '购买': ['是', '否', '是', '是', '否', '否', '是', '否']
}
df = pd.DataFrame(data)
crosstab = pd.crosstab(df['性别'], df['购买'])# 创建交叉表
print(crosstab)

# 透视表是将原有的DataFrame的列分别作为行索引和列索引，然后对指定的列应用聚集函数
data = {
    '性别': ['男', '女', '男', '女', '男', '女'],
    '购买': ['是', '否', '是', '是', '否', '否'],
    '金额': [100, 150, 200, 130, 160, 120]
}
df = pd.DataFrame(data)
pivot_table = pd.pivot_table(df, values='金额', index='性别', columns='购买', aggfunc='mean')# 创建透视表
print(pivot_table)

# 准备两列数据，星期数据以及涨跌幅是好是坏数据
# 进行交叉表计算
data = pd.read_csv("./data/stock_day.csv", usecols=['p_change'])
# 寻找星期几跟股票涨跌的关系
date = pd.to_datetime(data.index).weekday # 先把对应的日期找到星期几
data['week'] = date
data['posi_neg'] = np.where(data['p_change'] > 0, 1, 0) # 假如把p_change按照大小去分个类0为界限
print(data.head(10))
# 通过交叉表找寻两列数据的关系
count = pd.crosstab(data['week'], data['posi_neg'])
print(count)

# 但是我们看到count只是每个星期日子的好坏天数，并没有得到比例，该怎么去做？
# 对于每个星期一等的总天数求和，运用除法运算求出比例
sum = count.sum(axis=1).astype(np.float32) # 算数运算，先求和
print(sum)
pro = count.div(sum, axis=0) # 进行相除操作，得出比例
print(pro)

pro.plot(kind='bar', stacked=True)
plt.show()

# 使用pivot_table(透视表)实现，刚才的过程更加简单
data.pivot_table(['posi_neg'], index='week') # 通过透视表，将整个过程变成更简单一些
print(data)