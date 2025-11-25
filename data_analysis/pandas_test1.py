import numpy as np
import pandas as pd
# Pandas中有两大核心对象, 分别是: DataFrame和Series, 其中, Series -> 一列数据, DataFrame -> 多列数据

# 1. 创建Series对象, 采用: 默认自增索引.
s1 = pd.Series([1,2,3,4,5])
print(s1)
print(s1[1])
print(s1.iloc[1])

# 2. 创建Series对象, 采用: 自定义索引.
s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s2)
print(s2['c'])
print(s2.iloc[2:5])

# 3. 使用字典, 元组创建Series对象.
# 元组形式
s3 = pd.Series((11, 22, 33, 44, 55))
print(s3)

# 字典形式.
s4 = pd.Series({'a': 1, 'b': 3, 'c': 5})
print(s4)

# 4. 使用numpy -> 创建Series对象.
s5 = pd.Series(np.arange(5))
print(s5)

# 2.2 Series对象的属性
# 1. 构建Series对象, 索引为: A-F, 值为: 0-5
s6 = pd.Series(data=[0, 1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E', 'F'])
# 加入列表推导式
s6 = pd.Series(data=[i for i in range(6)], index=[i for i in 'ABCDEF'])
print(s6)

# 2. 获取Series对象的 索引列(的值)
print(s6.index)     # Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')

# 3. 获取Series对象的 值列(的值)
print(s6.values)

# 4. Series支持根据 索引 获取元素, 即: Series对象[索引值]
print(s6['D'])  # 3

# 5. 根据索引, 修改Series对象的 元素值
s6['D'] = 99
print(s6)

# 3. DataFrame对象入门
# 3.1 创建DataFrame对象
# 场景1: 通过 字典 + 列表的方式实现.
# 1. 准备数据集, 每个键值对 = 1列数据
info = {
    'name': ['水冷哥', '深情哥', '紫琪', '德华'],
    'gender': ['女', '男', '保密', '保密'],
    'age': [81, 80, 66, 55],
}
# 2. 把上述的数据集, 封装成DataFrame对象.
df1 = pd.DataFrame(data=info)
print(df1) # 打印结果.

# 场景2: 通过 列表 + 元组 的方式实现.
# 1. 准备数据集, 每个元组 = 1行数据
info = [
    ('刘亦菲', '女', 39),
    ('迪丽热巴', '女', 31),
    ('王志奇', '未知', 66),
]
# 2. 把上述的数据集, 封装成DataFrame对象.
df2 = pd.DataFrame(data=info, columns=['姓名', '性别', '年龄'])
print(df2) # 打印结果.

# 场景3: 通过 numpy的ndarray -> pandas DataFrame 的方式实现.
# 1. 创建numpy的 ndarray对象.
arr1 = np.arange(12).reshape(3, 4)
# print(arr1)
# 2. 把上述的ndarray对象, 封装成DataFrame对象.
df3 = pd.DataFrame(data=arr1, columns=['a', 'b', 'c', 'd'])
print(df3)

# 3.2 学生信息处理 -> DataFrame简单案例
# 1. 生成10名同学, 5门功课的成绩, 成绩范围: 40 ~ 100
score_df = pd.DataFrame(np.random.randint(40, 101, (10, 5)))    # 10行, 5列   包左不包右
print(score_df)

# 2. 修改DataFrame对象的 列名 和 索引列值.
column_names = ['语文', '数学', '英语', '政治', '体育']

# index_names = ['同学0', '同学1', '同学2', '同学3', '同学4', '同学5', '同学6', '同学7', '同学8', '同学9']
index_names = ['同学' + str(i) for i in range(score_df.shape[0])]

# 3. 具体的修改DataFrame对象 列名 和 索引值的动作.
# score_df.columns = column_names
# score_df.index = index_names

# rename函数也可以.
# score_df.rename(index={0:'同学0', 1:'同学1'}, columns={0: 'AI课程', 1: '大数据课程'}, inplace=True)

#                     i的值: 0 ~ 9                                                               i的值: 0 ~ 4
score_df.rename(
     index={i:index_names[i] for i in range(score_df.shape[0])},
     columns={i: column_names[i] for i in range(score_df.shape[1])},
     inplace=True
 )
print(score_df) # 打印修改后的结果.

# 3.3 DataFrame的基本属性
# shape 维度, 即: 行列数
print(score_df.shape)   # (10, 5)
# index: 索引列
print(score_df.index)
# columns: 列名
print(score_df.columns)
# values: 数据(值)
print(score_df.values)
# 行列转置, T
print(score_df.T)

# 3.4 DataFrame的基本函数
# 1. head(n), 查看前n行数据
# score_df.head()     # 默认是 5 条
print(score_df.head(3))      # 指定数据条数

# 2. tail(n), 查看后n行数据
# score_df.tail()     # 默认是 5 条
print(score_df.tail(2))   #  指定数据条数

# 3. info(), 查看df对象的详细信息
print(score_df.info())

# 4. describe(), 查看df对象的 描述性 统计信息
print(score_df.describe())

# 5. reset_index() 重置索引列.
# score_df1 = score_df.reset_index(drop=False)    # drop=False, 默认值, 不删除原索引列.
score_df1 = score_df.reset_index(drop=True)       # drop=True, 删除原索引列.
print(score_df1)

# 6. set_index(): 重新设置索引.
# score_df2 = score_df.set_index('语文')        # 语文成绩充当索引列.
# 语文, 英语充当索引列.
score_df2 = score_df.set_index(['语文', '英语'])
print(score_df2)

# 3.5 Pandas的数据类型介绍
# Pandas中的数据类型几乎和Python中是一致的, 只不过有几个不太一样.
# 例如: Python: str -> Pandas: object,  Python: None -> Pandas: nan,NAN,NaN,
# Pandas还支持category分类类型, 针对于分类数据操作更快, 更节省内存.
# 1. 创建DataFrame对象.
df = pd.DataFrame({
    'name': [np.nan, '深情哥', '紫琪', '德华'],
    'gender': ['女', '男', '保密', np.nan],
    'age': [81, 80, np.nan, 55]
})
print(df)

# 2. 查看df对象的 详细信息
print(df.info())

# 3. 演示 日期类型 datetime
df2 = pd.DataFrame(['2025-03-29', '2025-03-30', '2025-03-31'], dtype='datetime64[ns]')
print(df2)
print(df2.dtypes)

# 4. 演示 日期差类型 timedelta
start_date = pd.to_datetime('2004-08-21')
end_date = pd.to_datetime('2025-03-29')
print(end_date - start_date) # 打印结果
print(type(end_date - start_date))

# 5. 演示下 category类型
s1 = pd.Series(['男', '女', '保密'], dtype='category')
print(s1)
print(type(s1))
print(s1.dtypes)    # category

# 4.Pandas的基本操作
# 4.1 加载数据
# 1. 加载数据
df = pd.read_csv('./data/stock_day.csv')
# print(df)

# 2. 移除不需要的字段.
df.drop(columns=['ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20'], axis=0, inplace=True)   # 0: 列, 1: 行
# 3. 查看处理后的数据.
# print(df.head())              # 查看数据.
# print(df.info())       # 查看详细信息
# print(df.describe())   # 查看描述性统计信息

# 4.2 索引操作
# 场景1: 根据行列索引获取元素, 先列后行.
print(df['open']['2018-02-23'])    # 22.88
# 尝试用: 先行后列
# print(df['2018-02-23']['open'])   # 错误写法

# 场景2: 结合 loc 根据: 行索引 和 列名 来获取元素.
# 格式: df.loc[行索引, 列名]
# 格式: df.iloc[行号, 列索引]
print(df.loc['2018-02-27', 'high'])        # 获取一条数据
print(df.loc['2018-02-27':'2018-02-14', ['open', 'high']])

# 场景3: 结合 iloc 根据: 行号 和 列索引 来获取元素.
print(df.iloc[0:5, 0:2])   # 获取多条数据
print(df.iloc[0:1, :])   # 获取多条数据

# 4.3 赋值操作
# 2. 赋值操作
df['open'] = 23
df.low = 1          # 效果同上, 更简单, 但是有弊端, 如果 字段有空格等, 该方式不行, 例如:  df.max value 必须写成 df['max value']
# print(df.low) #  查看结果

# 4.4 排序操作
# 2. 基于开盘价格做 升序 排列.
df1 = df.sort_values(by='close', ascending=True)   # 升序.
# print(df1)
df2 = df.sort_values(by='close', ascending=False)    # 降序.
# print(df2)

# 3. 基于开盘价格降序排列, 价格一样, 基于 当日最高价格(high) 降序排列.
df3 = df.sort_values(by=['close', 'high'], ascending=[False, False])
# print(df3)

# 4. 按照索引排序.
df4 = df.sort_index(ascending=True)   # 默认升序.
# print(df4)

# 5. 演示 Series对象也有 sort_index(), sort_values() 排序方法.
s0 = df['close']
# print(type(s0))
# print(s0.values)
# print(s0.index)
s1 = df.close.sort_index(ascending=True)    # 索引升序
# print(s1)
s2 = df.close.sort_values(ascending=False)    # 价格降序
# print(s2)

# 5. DataFrame的运算
# 5.1 算术运算
# 2. 针对于 close列值 + 100 处理.
df4 = df.close.add(100)       # 效果同下
df5 = df.close + 100        # Series对象 和 数值运算, 则 Series中的每个数值都会和该数字进行运算.
# print(df5)

# 3. 针对于 close列的值 - 100 处理
df6 = df.close.sub(100)
df7 = df.close - 100     # 效果同上
# print(df7)

# 5.2 逻辑运算符 &, |
# 2. 完成需求.
# 需求1: 筛选出 close列值 > 23的数据.
df8 = df[df.close > 34]
# print(df8)
# 需求2: 筛选出 close列值 > 23, 且 < 24的数据.
df9 = df[(df.close > 33) & (df.close < 34)]           # 细节: 多组判断记得加 小括号.
# print(df9)
df10 = df[(df['close'] > 33) & (df['close'] < 34)]     # 标准写法.
# print(df10)

# 3. 可以通过 query()函数, 优化上述的代码.
df11 = df.query('close > 33 & close < 34')
# print(df11)

# 4. 固定值的筛选, isin
# 需求: 查询 close价格为 23.53, 23.67价格数据.
# df12 = df[(df.close == 33.83) | (df.close == 33.34)]
df12 = df[df.close.isin([33.83, 33.34])]
# print(df12)

# df13 = df.query('close == 33.83 | close == 33.34')
df13 = df.query('close in [33.83, 33.34]')
print(df13)
