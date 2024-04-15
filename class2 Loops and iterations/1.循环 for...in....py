"""
循环
       for…in…
       range 函数
       for…else
    缩进对齐语法：必须对齐，不对齐不算在循环内
list   ：包含成员和下标
len 函数：统计值总数
range 函数生成连续规律的数值
"""
books = ["Python", "JavaScript", "Ruby", "pytest"]
for book in books:
    print(f"本次取出的书是: {book}")
    print("111")
    print("222")
    print("3333")
# 不对齐，不算在循环内
print("不算循环内")

# 循环下标，知道个数可以直接写书，不知道需要用len 函数先查询
# 从左往右0开始
for index in [0, 1, 2, 3]:
    print(f"下标：{index}")
    print(f"通过下标得到成员：{books[index]}")
# 从右往左-1开始
for index in [-1, -2, -3, -4]:
    print(f"下标：{index}")
    print(f"通过下标得到成员：{books[index]}")

# len 函数：统计值总数
print(len(books))
# range 函数生成连续规律的数值
print(list(range(4)))

# 使用len和range 函数来打印 下标和books的值
for index in range(len(books)):
    print(f"下标：{index}")
    print(f"通过下标得到成员：{books[index]}")
