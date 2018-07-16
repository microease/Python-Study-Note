# 还记得中学时候学过的杨辉三角吗？具体的定义这里不再描述，你可以参考以下的图形：
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# ..............
# 先在给你一个正整数n，请你输出杨辉三角的前n层
# 注意：层数从1开始计数,每层数字之间用一个空格隔开，行尾不要有空格。
# 如n=2,则输出：
# 1
# 1 1
#
# 详细定义
# 前提：每行端点与结尾的数为1.
# 每个数等于它上方两数之和。
# 每行数字左右对称，由1开始逐渐变大。
# 第n行的数字有n项。
# 第n行数字和为2n-1。
# 第n行的m个数可表示为 C(n-1，m-1)，即为从n-1个不同元素中取m-1个元素的组合数。
# 第n行的第m个数和第n-m+1个数相等 ，为组合数性质之一。
# 每个数字等于上一行的左右两个数字之和。可用此性质写出整个杨辉三角。即第n+1行的第i个数等于第n行的第i-1个数和第i个数之和，这也是组合数的性质之一。即 C(n+1,i)=C(n,i)+C(n,i-1)。
# (a+b)n的展开式中的各项系数依次对应杨辉三角的第(n+1)行中的每一项。
# 将第2n+1行第1个数，跟第2n+2行第3个数、第2n+3行第5个数……连成一线，这些数的和是第4n+1个斐波那契数；将第2n行第2个数(n>1)，跟第2n-1行第4个数、第2n-2行第6个数……这些数之和是第4n-2个斐波那契数。
# 将各行数字相排列，可得11的n-1（n为行数）次方：1=11^0; 11=11^1; 121=11^2……当n>5时会不符合这一条性质，此时应把第n行的最右面的数字"1"放在个位，然后把左面的一个数字的个位对齐到十位... ...，以此类推，把空位用“0”补齐，然后把所有的数加起来，得到的数正好是11的n-1次方。以n=11为例，第十一行的数为：1,10,45,120,210,252,210,120,45,10,1，结果为 25937424601=1110。
# 求和函数
# print(sum([1,2,3]))
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = zip(a,b)
# for i in c:
#     print(i)
# c = [sum(i) for i in zip(a, b)]
# for i in c:
#     print(i)

def YangHui():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

n = 0
for j in YangHui():
    print(j)
    n += 1
    if n == 10:
        break
