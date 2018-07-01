# 给你一个整数组成的列表L，按照下列条件输出：
# 若L是升序排列的,则输出"UP";
# 若L是降序排列的,则输出"DOWN";
# 若L无序，则输出"WRONG"。
L = [1, 2, 32, 421, 242, 1424, 55353, 312421]
if L == sorted(L):
    print("UP")
elif L == sorted(L, reverse=True):
    print("DOWN")
else:
    print("WRONG")