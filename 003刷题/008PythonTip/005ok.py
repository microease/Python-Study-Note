# 给你一个字符串 a， 输出a中奇数位置字符构成的字符串（位置编号从1开始）。
# 例如：a=‘xyzwd’
# 则输出:xzd
a = "xyzwd"
b = []
lena = len(a)
for i in range(1, lena + 1):
    if i % 2 != 0:
        b.append(a[i-1])
    else:
        continue

print("".join(b))
