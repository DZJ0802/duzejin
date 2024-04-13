"""
转义字符"\"反斜杠
"\\" 两个反斜杠 转义为 "\" 一个反斜杠
"\n"换行
"\t"table键
\ 加双引号
\ 加单引号
\a 电脑执行后会响铃
\b 退格键（Backspace）
\v 纵向制表符
\t 横向制表符
\r 回车 将\r 后面字符替换前面字符
\f 换页
\yyy 八进制数，y代表0-7的字符，例如：\012 代表换行
"""
# 1.换行打印内容Hello world
print('hello\nworld')

# 2.打印的字符串有单引号和双引号
print('hello \"world\", \'yo\'  ')

# 3.打印一个 \ 字符
print('\\')

# 4.打印一个路径，带有反斜杠 \的时候
# 我有个路径D:\new\row 第一个写的这样错误的
# 错误：print('D:\new\row')
# 需转义
print('D:\\new\\row')
# raw 原始数据不需要转义
print(r'D:\\new\\row')

# 5.\a 电脑执行后会响铃
print("\a")

# 6.\b 退格键（Backspace）
print("6Hello \b World")

# 7.\v 纵向制表符
print("7Hello \v World")

# 8.\t 横向制表符
print("8Hello \t World")

# 9.\r 回车
print("9Hello\rWorld")

# 10.\f 换页
print("10Hello \f World")

# 11.\yyy 八进制数，y代表0-7的字符，例如：\012 代表换行
# print("\110\145\154\154\157\40")

