# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

# 列表sort方法：
# l = []
# for i in range(3):
#     x = int(input("请输入三个整数，以回车切换\r\n"))
#     l.append(x)
# l.sort()
# print(l)

#笨办法
# x = int(input("请输入x的值，x是整数\n"))
# y = int(input("请输入y的值，y是整数\n"))
# maxXy = max(x,y)
# minXy = min(x,y)
# z = int(input("请输入z的值，z是整数\n"))
# if z > maxXy:
#     print(minXy,maxXy,z)
# elif z < minXy:
#     print(z,minXy,maxXy)
# else:
#     print(minXy,z,maxXy)

#冒泡排序
# 冒泡排序算法的原理如下：
# 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
# 针对所有的元素重复以上的步骤，除了最后一个。
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
x = int(input("请输入x的值，x是整数\n"))
y = int(input("请输入y的值，y是整数\n"))
z = int(input("请输入z的值，z是整数\n"))
arrXyz = [x,y,z]
print(len(arrXyz))
def maoPao(num):
    for i in range(len(num)-1):#控制循环次数
        for j in range(len(num)-i-1):
            if num[j]>num[j+1]:
                num[j+1],num[j] = num[j],num[j+1]
    return num
print(maoPao(arrXyz))

