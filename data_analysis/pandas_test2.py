import numpy as np
import pandas as pd
# read_csv: pandas.read_csv(filepath_or_buffer, sep =',', usecols )
# filepath_or_buffer:文件路径
# sep:分隔符，默认用","隔开
# usecols:指定读取的列名，列表形式
# 举例：读取之前的股票的数据 - 读取文件,并且指定只获取'open', 'close'指标
data = pd.read_csv("./data/stock_day.csv", usecols=['open', 'close'])
# print(data)

data1 = pd.read_csv('./data/stock_day.csv', sep=',', index_col=[0])
# print(data1)

# to_csv: DataFrame.to_csv(path_or_buf=None, sep=', ’, columns=None, header=True, index=True, mode='w', encoding=None)
# path_or_buf :文件路径
# sep :分隔符，默认用","隔开
# columns :选择需要的列索引
# header :boolean or list of string, default True
# index:是否写进行索引,是否写进列索引值
# mode:'w'：重写, 'a' 追加
# 举例：保存读取出来的股票数据 - 保存'open'列的数据，然后读取查看结果
data[:10].to_csv("./data/test.csv", columns=['open']) # 选取10行数据保存,便于观察数据
# index:存储不会讲索引值变成一列数据
data[:10].to_csv("./data/test1.csv", columns=['open'], index=False)

# DataFrame数据的增删改查操作
df = pd.read_csv('./data/1960-2019全球GDP数据.csv', encoding='gbk')
df2 = df.head()
# 增加列
# 方式一: 通过直接赋值的方式添加新列
# 拷贝一份df
df3 = df2.copy()
# 一列数据都是固定值
df3['new col 1'] = 33
# 新增列数据数量必须和行数相等
df3['new col 2'] = [1, 2, 3, 4, 5]
df3['new col 3'] = df3.year * 2
# 分别查看增加数据列之后的df和原df
# print(df2)
# print(df3)

# 方式二: df.assign函数添加列
# 1. 新列名=单个数据或一组数据，一组数据的数量必须和df的行数相同
df4 = df2.assign(new0=66)
# df2.assign(new1=[1, 2, 3, 4]) # 报错
df2.assign(new1=[1, 2, 3, 4, 5])

# 2.1 新列名=Series对象，该s对象的索引和df索引一致
s = pd.Series([1, 2, 3, 4, 5])
df2.assign(new2=s)

# 2.2 新列名=Series对象
df2.assign(new3=df2.year+df2.GDP)

# 3. 新列名=自定义函数名 - 该自定义函数必须接收df作为参数
# 该自定义函数可以返回：
# 3.1.单个数据
# 3.2.一组数量和df的行数相同的数据
# 3.3.和df索引相同的Series对象
def foo(df): # 函数必须接收一个参数，该参数就是被传入的df对象
    print('='*10)
    print(df)
    print('='*5 + '上面输出的是传入的df')
    ret = df.index.values
    # 可以返回一个变量
    # return 'hahah'
    # 也可以返回一组变量
    return ret
df4 = df2.assign(new4=foo)
# print(df4)

# df.assign函数可以同时添加多列
def foo(df):
    return 22

def bar(df):
    return df.year + 1

df5 = df2.assign(
    new0='hahaha',
    new1=[1, 2, 3, 4, 5],
    new2=pd.Series([1, 2, 3, 4, 5]),
    new3=df.year*2,
    new4=foo,
    new5=bar
)
# print(df5)

# 删除与去重
# df.drop删除行数据
# print(df3)
df3.drop([0]) # 默认删除行
# df6 = df3.drop([0, 2, 4]) # 可以删除多行
df6 = df3.GDP.drop([0, 2]) # 对series对象按索引删除
# print(df6)

#  df.drop删除列数据 - df.drop默认删除指定索引值的行；如果添加参数axis=1，则删除指定列名的列
df7 = df3.drop(['new col 3'], axis=1)
#print(df7)

# 使用del删除指定的列
# 注意区别：del是直接永久删除原df中的列【慎重使用】
#           drop是返回删除后的df或seires，原df或seires没有被修改
del df3['new col 3']
# print(df3)

# dataframe数据去重 - 添加一部分重复的数据
df4 = df._append(df).reset_index(drop=True)
# print(df4)
# 实施去重操作
df8 = df4.drop_duplicates()
# print(df8)

# series去重
# 方式一:
df9 = df4.country.drop_duplicates()
# print(df9)
# 方式二:
df10 = df4.country.unique()
# print(df10)

# 修改DataFrame中的数据
df11 = df5.assign(GDP=66) # 可以接收单变量或列表、数组
# print(df11)
# 直接对原始的DF进行赋值修改处理 - 一般不建议直接修改操作
df5['GDP'] = [5, 4, 3, 2, 1]
# print(df5) # 此时原始的df会发生改变

# replace函数替换数据
df5.year.replace(1960, 19600) # series对象替换数据，返回的还是series对象，不会对原来的df造成修改
# 如果加上inplace=True参数，则会修改原始df
df5.country.replace('日本', '扶桑', inplace=True)
print(df5)
# df也可以直接调用replace函数，用法和s.replace用法一致，只是返回的是df对象
df12 = df5.replace(1960, 19600) # 备注：replace()是按照单元格元素值进行完全匹配
print(df12)

# 查询dataFrame中的数据
# 从前从后取多行数据
df.head()# 默认取前5行数据
# print(df.head(10)) # 取前10行
df.tail()# 默认取后5行数据
df2 = df.tail(15) # 倒数15行
# print(df2)

# 获取一列或多列数据 - 获取一列数据df[col_name]等同于df.col_name
# print(df2['country']) # 注意！如果列名字符串中间有空格的，只能使用df['country']这种形式
# print(df2.country)

# 获取多列数据df[[col_name1,col_name2,...]]
# print(df2[['country', 'GDP']]) # 返回新的df

# 索引下标切片取行
# df[start:stop:step] == df[起始行下标:结束行下标:步长], 遵循顾头不顾尾原则 (包含起始行，不包含结束行), 步长默认为1
# print(df2[0:3]) # 取前3行
# print(df2[:5:2]) # 取前5行，步长为2
# print(df2[1::3]) # 取第2行到最后所有行，步长为3

# 查询函数获取子集: df.query()
# df.query(判断表达式)可以依据判断表达式返回的符合条件的df子集
# print(df3.query('country=="美国"'))# 特别注意df.query()中传入的字符串格式
# print(df3[df3['country']=='美国'])# 与df[布尔值向量]效果相同

# 查询中国, 美国 日本 三国 2015年至2019年的数据
# print(df5.query('country=="中国" or country=="日本" or country=="美国"').query('year in [1960, 2016, 2017, 2018, 2019]'))
# print(df5.query('(country=="中国" or country=="日本" or country=="美国") and year in [1960, 2016, 2017, 2018, 2019]'))

# 排序函数 - sort_values函数: 按照指定的一列或多列的值进行排序
# 按GDP列的数值由小到大进行排序
# print(df2.sort_values(['GDP']))
# 按GDP列的数值由大到小进行排序
# print(df2.sort_values(['GDP'], ascending=False)) # 倒序， ascending默认为True
# 先对year年份进行由小到大排序，再对GDP由小到大排序
# print(df2.sort_values(['year', 'GDP']))

# rank函数
df2.rank()
df2.rank(axis=0)
df2.rank(numeric_only=True) # 只对数值类型的列进行统计
df2.rank(ascending=False) # 降序
df2.rank(pct=True) # 以最高分作为1，放回百分数形式的评分，pct参数默认为False
df2.rank(method='average') # 排名评分的计算方式
df2.rank(method='min')
df2.rank(method='max')
df2.rank(method='dense')

df7 = pd.DataFrame({
    '姓名':['小明', '小美', '小强', '小兰'],
    '成绩':[100, 90, 90, 80]
})
df7.rank() # 等价于df7.rank(method='average', ascending=True)
df7['成绩排名'] = df7.成绩.rank(method='min', ascending=False)
# df7['成绩排名'] = df7.成绩.rank(method='max', ascending=False)
# df7['成绩排名'] = df7.成绩.rank(method='dense', ascending=False)
# print(df7)

# 聚合函数
# print(df2['year'].min()) # min函数
# print(df2['year'].max()) # max函数
# print(df2['year'].mean()) # mean平均值
# print(df2['GDP'].mean())

# 缺失值处理
# 电影数据的缺失值处理
movie = pd.read_csv("./data/movie.csv")
# 判断缺失值是否存在
# print(pd.notnull(movie))
# print(np.all(pd.notnull(movie)))
# print(pd.isnull(movie))
# print(np.any(pd.isnull(movie)))

# 存在缺失值nan,并且是np.nan
# 不修改原数据
movie.dropna()
# 可以定义新的变量接受或者用原来的变量名
data = movie.dropna()

#获取空值行
row_with_null = movie.isnull().any(axis=1)
# print(row_with_null)
# print(movie[row_with_null])

# 替换缺失值
# 替换存在缺失值的样本的两列, 替换填充平均值，中位数
# movie['Revenue (Millions)'].fillna(movie['Revenue (Millions)'].mean(), inplace=True)
# movie['Metascore'].fillna(movie['Metascore'].mean(), inplace=True)
# print(movie[row_with_null])

# 替换所有缺失值
for column in movie.columns:
    if np.all(pd.notnull(movie[column])) == False:
        print(column)
        movie[column].fillna(movie[column].mean(), inplace=True)
# print(movie[row_with_null])

# 不是缺失值nan，有默认标记的
wis = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data")
# print(wis.shape)
# 处理思路分析：
# 1、先替换'?'为np.nan
# df.replace(to_replace=, value=) # to_replace:替换前的值, value:替换后的值
wis = wis.replace(to_replace='?', value=np.nan)# 把一些其它值标记的缺失值，替换成np.nan
# 2、在进行缺失值的删除处理
wis = wis.dropna()
# print(wis.shape)