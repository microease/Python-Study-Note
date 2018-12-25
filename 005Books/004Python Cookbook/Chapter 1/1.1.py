# 解压序列赋值给多个变量
p = (4, 5)
x, y = p
print(x, y)

data = ['ACME', 50, 90.1, (2018, 12, 25)]
name, shares, price, (year, month, day) = data
print(name, shares, price, year, month, day)

s = 'hello'
a, b, c, d, e = s
print(a, b, c, d, e)

# 占位符
data = ['ACME', 50, 90.1, (2018, 12, 25)]
_, shares, price, _ = data
print(shares, price)
