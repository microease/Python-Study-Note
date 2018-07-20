# 给你三个整数a,b,c,  判断能否以它们为三个边长构成三角形。
# 若能，输出YES，否则输出NO。
#此处使用三角形的定律，三角形的两条边长的和大于第三条边
L=[]

for i in range(3):
    a = input("请输入三角形的边")
    L.append(a)
L=sorted(L)
if (L[0]+L[1]>L[2]):
    print("YES")
else:
    print("NO")