"""
python会根据你写的值，默认定义值类型
a1 = 20 数字int  不可变类型
a2 = "Hello" string 字符串  不可变类型
a3 = [1, 2, 3] list 列表  可变类型
a4 = {"age": 22} dict字典  可变类型
a5 = (1, 2, 3) Tuple元组  不可变类型
"""
a1 = 20
a2 = "Hello"
a3 = [1, 2, 3]
a4 = {"age": 22}

# 多变量赋值  "="相同
a = b = c = 123
print(a)
print(b)
print(c)

# ","解构赋值 ，分成多个顺序赋值
x, y = "hello", "world"
print(x)
print(y)

x1, y1 = ["hello", "world"]
print(x1)
print(y1)

x2, y2 = ("hello", "world")
print(x2)
print(y2)