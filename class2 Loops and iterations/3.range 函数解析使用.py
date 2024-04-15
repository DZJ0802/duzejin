"""
range包含(start 起始位置, stop 终点位置, step 步长)
例如：
range(5) (start=0 , stop=5 , step=1)
range(1, 5) (start=1 , stop=5 , step=1)
range(1, 5, 2) (start=1 , stop=5 , step=2)
"""
x = range(1, 5, 2)  # [0,1,2,3,4] ,随意定值生成自己想要生成的连续规律数值
print(x)  # range(0, 5)
for i in x:
    print(i)

# 从大到小排序的话

y = range(10, 0, -2)
for j in y:
    print(j)