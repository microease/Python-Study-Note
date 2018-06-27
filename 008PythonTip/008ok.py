# 给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）。
# 例如： L=[0,1,2,3,4]
# 则输出：2
# 结题思路
# 列表中元素的数量可能是偶数也可能是奇数，要考虑到这个情况
# 当列表中元素的数量是偶数的时候，中位数是最中间的两个数除以二
# 当列表中元素的熟练是奇数的时候，中位数是最中间的数字
L = [0, 1, 2, 3, 4]
L.sort()
if len(L) % 2 == 0:
    print(L[len(L)/2-1]+L[len(L)/2])/2
else:
    print(L[int((len(L)-1)/2)])