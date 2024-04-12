"""
字符串3种语法
"""
name = "yoyo"
age = 23

# 1: %s 格式化
print("my name is %s , my age is %s" % (name, age))

# 2: format 格式化{}内填写 0 ,1 ,2 可以选择第几个值
print("my name is {0} , my age is {1}" .format(name, age))

# 3: f-string  (推荐，性能最好)
print(f"my name is {name} , my age is {age}")