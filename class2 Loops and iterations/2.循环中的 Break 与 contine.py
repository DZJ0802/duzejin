"""
for 里面：Break 与 contine
Break 结束循环
Continue 跳过当次循环
"""
x = [1, 4, 71, 9, 0, 11, 45, 46]
for i in x:
    if i > 10:
        break   # 结束for循环
    else:
        print(f"成员:{i}")

for i in x:
    print(f"本次循环的i成员是:{i}")
    if i > 10:
        continue  # 跳过当前for循环，继续下一个
    else:
        print(f"成员:{i}")