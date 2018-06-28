# 给你一个整数列表L,判断L中是否存在相同的数字，
# 若存在，输出YES，否则输出NO。
#此题使用python的set函数，删除重复元素，形成集合
L = [1,4,23,24,23,54]
if len(L) == len(set(L)):
    print("NO")
else:
    print("YES")