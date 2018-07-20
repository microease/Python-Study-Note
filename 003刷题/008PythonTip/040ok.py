# 给你两个整数a和b（-10000<a,b<10000），请你判断是否存在两个整数，他们的和为a，乘积为b。
#  	若存在，输出Yes,否则输出No
#  	例如：a=9,b=15, 此时不存在两个整数满足上述条件，所以应该输出No。
# x + y = a
# x * y = b
# y = a - x
# x(a - x) = b
# x * a - x ** 2 = b
a = 9
b = 15
flag = 0
for x in range(-20000, 20000):
    if x * a - x ** 2 == b:
        m = m + 1
        print("YES")
        break
    if flag == 0:
        print("NO")