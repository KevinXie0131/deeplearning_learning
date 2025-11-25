import pandas as pd
#import os
#os.chdir(r'C:\Backup\Tech\黑马_数据处理和统计分析（Python数据分析）\05_Pandas基础\4.代码\pandasProject')   # 修改相对路径的位置.
#print(os.getcwd())

# 解决中文显示问题，下面的代码只需运行一次即可
import matplotlib as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 如果是Mac本, 不支持SimHei的时候, 可以修改为 'Microsoft YaHei' 或者 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False

# 1.1 折线图绘制 GDP变化趋势
# 1. 读取数据.
# 绝对路径
# df = pd.read_csv(r'D:\workspace\ai_23_work_bj\pandasProject\data\1960-2019全球GDP数据.csv', encoding='gbk')

# 相对路径
df = pd.read_csv('./data/1960-2019全球GDP数据.csv', encoding='gbk')
#print(df)

# 2. 加载中国的数据.
china_df = df[df.country == '中国']
# print(df.country)
# print(df['country'])
# print(china_df)

# 3. 设置 year字段为 索引列.
china_df.set_index('year', inplace=True)    # inplace=True, 表示修改原数据.
# print(china_df)

# 4. 绘制折线图
# china_df.plot()
china_df.GDP.plot()

# 5. 参考上述思路, 绘制中美日 三国GDP折线图.
usa_df = df[df.country == '美国'].set_index('year')
jp_df = df[df.country == '日本'].set_index('year')
# print(usa_df)
# print(jp_df)

# 6. 绘制三国折线图
china_df.GDP.plot()
usa_df.GDP.plot()
jp_df.GDP.plot()

# 1.2 绘制中美日三国 GDP 折线图, 加入图例 -> 拼音
# 1. 获取中美日三国的数据.
china_df = df[df.country == '中国'].set_index('year')
usa_df = df[df.country == '美国'].set_index('year')
jp_df = df[df.country == '日本'].set_index('year')
# print(china_df)

# 2. 分别修改 中美日三国的 GDP字段名为: 'china', 'usa', 'jp'
china_df.rename(columns={'GDP': 'china'}, inplace=True)
usa_df.rename(columns={'GDP': 'usa'}, inplace=True)
jp_df.rename(columns={'GDP': 'jp'}, inplace=True)
# 3. 查看修改后的数据
# print(china_df)

# 4. 绘制折线图.
china_df.china.plot(legend=True)    # 设置图例
usa_df.usa.plot(legend=True)
jp_df.jp.plot(legend=True)

# 1.3 绘制中美日三国 GDP 折线图, 加入图例 -> 中文
# 1. 获取中美日三国的数据.
china_df = df[df.country == '中国'].set_index('year')
usa_df = df[df.country == '美国'].set_index('year')
jp_df = df[df.country == '日本'].set_index('year')

# 2. 分别修改 中美日三国的 GDP字段名为: '中国', '美国', '日本'
china_df.rename(columns={'GDP': '中国'}, inplace=True)
usa_df.rename(columns={'GDP': '美国'}, inplace=True)
jp_df.rename(columns={'GDP': '日本'}, inplace=True)
# 3. 查看修改后的数据
# print(china_df)

# 4. 绘制折线图.
china_df.中国.plot(legend=True)    # 设置图例
usa_df.美国.plot(legend=True)
jp_df.日本.plot(legend=True)