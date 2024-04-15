"""
可迭代对象 Iterable
基本类型：list、str、tuple、dict、set
函数对象 range
"""
a = ["Holle", "Play Wright"]  # list 列表
b = "Python"  # string 字符串
c = 423   # 'int' object is not iterable
d = ("pytest", "324")  # Tuple元组
e = {"key": "333"}  # dict字典
f = {11, 32, 55}  # set 集合

for i in f:
    print(i)

for j in range(5):
    print(j)
