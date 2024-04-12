"""
list,相当于一个盒子，
 改变里面的值，外面盒子的id不会变化，
 只会对里面已修改的值的id发生变化；
f --> format 格式化
"""
x = ["hello", "world"]

print(f"x的id :{id(x)}")
print(x[0], x[1])
print(f"x0的id :{id(x[0])}  x1的id ：:{id(x[1])}")
x[0] = 'abx'

print(f"x的id :{id(x)}")