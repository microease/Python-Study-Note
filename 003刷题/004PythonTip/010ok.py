# 给你两个正整数a和b， 输出它们的最小公倍数。
# 例如：a = 3, b = 5
# 则输出：15
a = 3
b = 5
# #数学公式：两个数的乘积等于这两个数的最大公约数与最小公倍数的积
# 偷懒的解法
min = min(a,b)
for i in range(1,min):
    if (a%i)==0 and (b%i)==0:
        zdgys = i
zxgbs = (a*b)/zdgys
print(zxgbs)