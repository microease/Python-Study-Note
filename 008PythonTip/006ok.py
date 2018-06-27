# 输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。
# 质数又称素数，有无限个。质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。
list_sushu = []
for i in range(2,101):# 此处循环2到100
    for j in range(2,i):# 此处循环2到i
        if i%j==0:
            break
    else:
        list_sushu.append(i)
list_sushu = set(list_sushu)#列表去重
list_sushu = map(str,list_sushu)#map方法将字符串映射成字符串
list_sushu = " ".join(list_sushu)#join方法加空格
print(list_sushu)
