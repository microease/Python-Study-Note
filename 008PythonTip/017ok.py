# 给你两个正整数a,b,  输出它们公约数的个数。
# 例如：a = 24， b = 36
# 则输出：6
a = 24
b = 36
ans=0
for i in range(1,min(a,b)+1):
    if((a%i==0)and(b%i==0)):
        ans+=1
print(ans)