"""
可变 与 不可变
不可变：str 是不可变的
可变：list (相当于大箱子，里面内容可变)
"""
name = "yoyo"
new_name = name

print(f"name 的id : {id(name)}")
print(f"new_name 的id : {id(new_name)}")

name = "yoyo du"
print(f"name 的id : {id(name)}")
print(f"new_name 的id : {id(new_name)}")

"""可变"""
x = ["a", "b", "c"]
new_x = x

x[0] = 'abc'
print(x)
print(new_x)