import time  # 时间库
import numpy as np  # numpy库
import pandas as pd  # pandas库
from pyecharts.charts import Bar3D # 3D柱形图

# 1. 定义变量, 记录表名.
sheet_names = ['2018', '会员等级']

# 2. 读取5个excel表中的数据.
sheet_datas = pd.read_excel('./data/sales.xlsx', sheet_name=sheet_names)
print(sheet_datas)  # 共计: 154385行, 2列.
print(type(sheet_datas))  # 查看变量类型: dict,   结果是字典形式: 键: Excel表格名, 值: 该表格的数据.

# 3. 查看下 2015年的数据
print(sheet_datas['2018'])

# 4. 遍历, 查看数据(每个表格)的基本情况
for i in sheet_names:
    print(f'==================" + {i} + "======================', type(sheet_datas[i]))
    print(sheet_datas[i].head())
    print('==================" + info + "======================')
    print(sheet_datas[i].info())
    print('==================" + describe + "======================')
    print(sheet_datas[i].describe())

# 数据清洗, 即: 删除缺失值, 去掉异常值.
# 获取表名, 即: 2018, 不要最后的"会员等级"
for i in sheet_names[:-1]:
    # 2. 删除缺失值.
    sheet_datas[i] = sheet_datas[i].dropna()  # 删除缺失值.
    # 3. 去掉订单金额小于1的数据.
    sheet_datas[i] = sheet_datas[i][sheet_datas[i]['订单金额'] > 1]
    # 4. 创建新的字段, 用来记录每个sheet最后一笔消费的时间.
    # 其实就是每年的 12月31日
    sheet_datas[i]['max_year_date'] = sheet_datas[i]['提交日期'].max()

# 查看清洗后的数据
# 遍历表格名列表, 获取到每个表格名
for i in sheet_names:
    # 2. 查看是否还有 空值 数据.
    print(sheet_datas[i].isnull().sum())  # 统计空值数量, 都是0.
    # 3. 查看下每个表格, 订单金额列, 最小值都是 1元 以上的价格.
    print(sheet_datas[i].describe())

# 把前四年的数据, 拼接到一起
# sheet_datas.values() 字典的values()方法, 用于获取字典中所有的值(每个值, 都是1个df对象, 对应1个sheet表格)
# list(sheet_datas.values())        把上述的数据, 转成 列表形式
# list(sheet_datas.values())[0:-1]  获取到除了最后一张表(会员登记表)的所有数据.
# pd.concat()                       把前四年的数据(4个df对象), 拼接到一起.
data_merge = pd.concat(list(sheet_datas.values())[0:-1])
# 2. 验证下上述的数据, 看下每年具体多少条数据.
data_merge['max_year_date'].value_counts()
# 3. 给拼接后的数据, 新增一列 year, 表示: 数据的年份.
data_merge['year'] = data_merge['提交日期'].dt.year
# 4. 给拼接后的数据, 新增一列, 表示: 提交订单的间隔时间.
# 结果是: timedelta64[ns]类型, 即: 364 days 这样的数据.
data_merge['date_interval'] = data_merge['max_year_date'] - data_merge['提交日期']
# 5. 去掉 date_interval列的 日期单位, 从 364 days => 364
# 结果是: int64类型, 即: 364 这样的数据.
data_merge['date_interval'] = data_merge['date_interval'].dt.days
# 6. 查看处理后的数据
print(data_merge.info())

# 添加间隔日期列
# 计算日期间隔天数（该订单日期距离当年最后1天的天数），并添加列（该列的数据类型为timedelta64[ns]）
data_merge['date_interval'] = data_merge['max_year_date'] - data_merge['提交日期']
# 转换日期间隔为数字
data_merge['date_interval'] = data_merge['date_interval'].dt.days
data_merge.head()

#分组后聚合计算
# 基于year、会员ID列做分组之后，分别对date_interval、提交日期、订单金额做不同的运算
# as_index=False表示重置索引

# 1. 根据年份, 会员id分组, 计算用户 最近一次购买的日期, 订单总数, 订单总金额.
rfm_gb = data_merge.groupby(['year', '会员ID'], as_index=False).agg({
    # R 求分组后date_interval列中最小值：计算当年该会员最后一次订单距离年末12月31日的间隔天数
    'date_interval': 'min',
    # F 订单频率，计算当年该会员一共消费多少次，对订单号列进行count计算
    '订单号': 'count',
    # M 计算订单总金额：计算当年该会员一共消费多少钱
    '订单金额': 'sum'
})
# 2. 修改列名
rfm_gb.columns = ['year', '会员ID', 'r', 'f', 'm']
# 3. 查看聚合计算后的值
rfm_gb.describe()   # r(最后一次购买日期) 越小越好,  f(订单总数), m(订单总金额)越大越好.

# 查看数据分布
# rfm_gb.iloc[:,2:]表示只选择rfm_gb的rfm三类数据，并返回新df，
# 再做.describe().T操作，查看数据分布情况
print(rfm_gb.iloc[:, 2:].describe().T)

# 通过观察数据分布情况，自定义区间边界，代码如下
# 自定义区间边界，划分为3个区间，注意起始边界小于最小值
r_bins = [-1, 79, 255, 365]
f_bins = [0, 2, 5, 130] 	# f数据的分布比较极端，所以这里采用较小的值
m_bins = [0, 69, 1199, 206252]

# RFM分箱得分
# 演示 pd.cut() 函数, 方便的将一列连续型数据切分成类别型(即: 把数据分成指定的n个区间, 包右不包左)
# pd.cut()
# 参1: 要切的数值, 参2: 要切分成几组 / 传入切分阈值的列表 如果传入的是数值, 会做等距的划分
# 参数labels: 切分之后, 每一个类别 对应的取值, 默认使用每组的阈值(最小, 最大] 来作为取值
# 参数include_lowest, 默认是False, 即: 不包括下限(左区间), 设置为True后, 即为包括左区间

# 发现, 把r列的数据, 自动划分成了3个区间: (-0.365, 121.667], (121.667, 243.333], (243.333, 365.0]
pd.cut(rfm_gb['r'], bins=3)
# 查看类型, 还是一个 Series对象.
type(pd.cut(rfm_gb['r'], bins=3))
# 给pd.cut()函数, 指定: 切割区间.
pd.cut(rfm_gb['r'], bins=r_bins)

# 具体的计算规则, labels参数, 设置每个分组对应的标签(即: 显示内容)
# f: recency(最近一次购买日期间隔), 值越小, 评分越高.
rfm_gb['r_label'] = pd.cut(rfm_gb['r'], bins=r_bins, labels=[3, 2, 1])
# f: frequency(购买频次), 值越大, 评分越高.
rfm_gb['f_label'] = pd.cut(rfm_gb['f'], bins=f_bins, labels=[1, 2, 3])
# m: monetary(购买总金额), 值越大, 评分越高.
rfm_gb['m_label'] = pd.cut(rfm_gb['m'], bins=m_bins, labels=[1, 2, 3])

# 也可以用如下的方式计算
# rfm_gb['r_label']=pd.cut(rfm_gb['r'],bins=r_bins, labels=[i for i in range(len(r_range)-1,0,-1)])
# rfm_gb['f_label']=pd.cut(rfm_gb['f'],bins=f_bins, labels=[i+1 for i in range(len(f)-1)])
# rfm_gb['m_label']=pd.cut(rfm_gb['m'],bins=m_bins, labels=[i+1 for i in range(len(m)-1)])

# 查看下计算后的结果.
rfm_gb['r_label'].value_counts().sum()  # 计算下数据条数, 看是否和r列的数据条数一致(其它两列也可以计算下)
rfm_gb

# 计算RFM组合
# 为了方便后续处理, 把r, f, m的标签 转换为 字符串类型.
rfm_gb['r_label'] = rfm_gb['r_label'].astype(str)
rfm_gb['f_label'] = rfm_gb['f_label'].astype(str)
rfm_gb['m_label'] = rfm_gb['m_label'].astype(str)
# 计算 rfm最终评分结果.
rfm_gb['rfm_group'] = rfm_gb['r_label'] + rfm_gb['f_label'] + rfm_gb['m_label']
rfm_gb
# 查看每年, 每种会员的总数.
rfm_gb.groupby(['year', 'rfm_group'])['会员ID'].count()

# 图形数据汇总
display_data = rfm_gb.groupby(['rfm_group','year'],as_index=False)['会员ID'].count()
display_data.columns = ['rfm_group','year','number']
display_data['rfm_group'] = display_data['rfm_group'].astype(np.int32)
display_data.head()

# 显示图形
from pyecharts.commons.utils import JsCode
import pyecharts.options as opts

# 颜色池
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']

range_max = int(display_data['number'].max())
c = (
    Bar3D()#设置了一个3D柱形图对象
    .add(
        "",#图例
        [d.tolist() for d in display_data.values],#数据
        xaxis3d_opts=opts.Axis3DOpts(type_="category", name='分组名称'),#x轴数据类型，名称，rfm_group
        yaxis3d_opts=opts.Axis3DOpts(type_="category", name='年份'),#y轴数据类型，名称，year
        zaxis3d_opts=opts.Axis3DOpts(type_="value", name='会员数量'),#z轴数据类型，名称，number
    )
    .set_global_opts( # 全局设置
        visualmap_opts=opts.VisualMapOpts(max_=range_max, range_color=range_color), #设置颜色，及不同取值对应的颜色
        title_opts=opts.TitleOpts(title="RFM分组结果"),#设置标题
    )
)
c.render() 		      #数据保存到本地的网页中.

# 保存RFM结果到Excel
rfm_gb.to_excel('sales_rfm_score1.xlsx', index=False)  # 保存数据为Excel, 不写出索引列