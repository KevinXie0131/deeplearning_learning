import numpy as np
# numpy -> 和数学操作相关的库, numpy的数组是多维的, 并且是固定类型的, numpy的数组是ndarray, 主要用于: 矩阵运算
# 1.1 创建ndarray对象
# 1. 创建numpy的 ndarray对象.
print(np.arange(15))
print(type(np.arange(15)))
arr1 = np.arange(15).reshape(3, 5)
print(arr1)

# 1.2 演示numpy的常用属性
print(f'numpy的轴: {arr1.ndim}')       # 2
print(f'numpy的维度: {arr1.shape}')    # (3, 5),  3行5列
print(f'numpy的元素类型: {arr1.dtype}') # int32
print(f'numpy的元素个数: {arr1.size}')  # 15
print(f'numpy的元素占用字节数: {arr1.itemsize}')    # 4
print(f'numpy的元素类型: {type(arr1)}')  #  <class 'numpy.ndarray'>

# 2.创建Numpy的ndarray对象
# 2.1 array()函数, 把Python列表 -> ndarray对象
# 1. 创建python列表对象.
my_list = [11, 22, 33, 44, 55]
print(type(my_list))    #  <class 'list'>

# 2. 把python列表 -> ndarray对象.
arr2 = np.array(my_list)
print(arr2)         # [11 22 33 44 55]
print(type(arr2))   # <class 'numpy.ndarray'>

print( np.array([[11, 22, 33, 44, 55],[1, 2, 3, 4, 5]]))
print( np.array([[11, 22, 33, 44, 55],[1, 2, 3, 4, 5]]).shape )
print(type(np.array([[11, 22, 33, 44, 55],[1, 2, 3, 4, 5]])) )

#2.2 arange()函数, 创建ndarray对象
# arange(起始, 结束, 步长, dtype=类型), 类似于 Pythong中的range()函数.
# 1. 创建ndarray对象.
arr3 = np.arange(0, 10, 2, dtype=np.int64)
# 2. 打印ndarray对象.
print(arr3)
print(type(arr3))
print(f'元素的类型: {arr3.dtype}')

# 2.3 随机数生成 ndarray对象
# 1. random.rand() 生成 0.0 ~ 1.0之间, 包左不包右的 随机小数矩阵.
arr4 = np.random.rand(3, 5)     # 3行5列
print(arr4)
print(type(arr4))

# 2. random.randint(起始值, 结束值, size=(行,列)) 生成指定范围, 包左不包右的 随机整数矩阵.
arr5 = np.random.randint(3, 9, size=(2, 6))     # 3 ~ 9之间, 包左不包右. 2行6列
print(arr5)
print(type(arr5))

# 3. random.uniform(起始值, 结束值, size=(行,列)) 生成指定范围, 包左不包右的 随机小数矩阵.
arr6 = np.random.uniform(3, 9, size=(2, 6))
print(arr6)
print(type(arr6))

# 4 ndarray的数据类型
arr7 = np.zeros((3, 4), dtype=np.float64)
print(arr7)
print(arr7.dtype)

# 5 等比/等差数列
print(np.logspace(0, 9, 10, base=2))
print(np.linspace(1, 10, 10)) # 等差数列

# 基本函数
# np.ceil(): 向上最接近的整数，参数是 number 或 array
# np.floor(): 向下最接近的整数，参数是 number 或 array
# np.rint(): 四舍五入，参数是 number 或 array
# np.isnan(): 判断元素是否为 NaN(Not a Number)，参数是 number 或 array
# np.multiply(): 元素相乘，参数是 number 或 array
# np.divide(): 元素相除，参数是 number 或 array
# np.abs()：元素的绝对值，参数是 number 或 array
# np.where(condition, x, y): 三元运算符，x if condition else y

# 统计函数
# np.mean(), np.sum()：所有元素的平均值，所有元素的和，参数是 number 或 array
# np.max(), np.min()：所有元素的最大值，所有元素的最小值，参数是 number 或 array
# np.std(), np.var()：所有元素的标准差，所有元素的方差，参数是 number 或 array
# np.argmax(), np.argmin()：最大值的下标索引值，最小值的下标索引值，参数是 number 或 array
# np.cumsum(), np.cumprod()：返回一个一维数组，每个元素都是之前所有元素的 累加和 和 累乘积，参数是 number 或 array
# 多维数组默认统计全部维度，axis参数可以按指定轴心统计，值为0则按列统计，值为1则按行统计。

arr8 = np.arange(12).reshape(3, 4)
print(arr8)
print(np.sum(arr8))
print(np.sum(arr8, axis=0)) # 按列统计
print(np.sum(arr8, axis=1)) # 按行统计

# 去重函数: np.unique():找到唯一值并返回排序结果，类似于Python的set集合
print(np.unique(np.array([[1,2,1],[2,3,4]])))

# 对数组元素进行排序
arr9 = np.array([11,2,34,5])
print(np.sort(arr9))

# 基本运算: 数组的算数运算是按照元素的。新的数组被创建并且被结果填充。
arr10 = np.arange(15).reshape(3, 5)
print(arr10)
arr11= np.arange(15, 30).reshape(3, 5)
print(arr11)
print(arr10 - arr11)

# 矩阵乘法 矩阵对应元素的乘法（multiplication by element-wise）
print(arr10 * arr11)
print(np.multiply(arr10, arr11))

# 矩阵点积
arr12 = np.arange(10).reshape(5, 2)
print(np.dot(arr10, arr12))