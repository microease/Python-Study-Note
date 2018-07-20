# 给你两个正整数a和b， 输出它们的最大公约数。
# 例如：a = 3, b = 5
a = 30
b = 60
min = min(a,b)
for i in range(1,min):
    if (a%i)==0 and (b%i)==0:
        zdgys = i
print(zdgys)
