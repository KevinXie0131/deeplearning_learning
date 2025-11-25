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
print(s2.iloc[2])

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