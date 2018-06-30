# 我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。注：所给数据都有解，不用考虑无解的情况。
# 例如：a=3, b = 60
# 则输出：12 15
a = 3
b = 60
# 最小公倍数 = 两数乘积/最大公约数
import math
minAb = min(a, b)  # 这个是最大公约数
maxAb = max(a, b)  # 这个是最小公倍数
list1 = []
for i in range(minAb, maxAb):
    for j in range(minAb, maxAb):
        if math.gcd(i, j) == a and i * j / a == b:  # 如果ij的最大公约数为a且最小公倍数为b
            list1.append((i, j))
list1.sort(key=lambda x: x[0] + x[1])  # 按最小和排序
print(" ".join(map(str, list1[0])))  # 输出第一组
