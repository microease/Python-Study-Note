# 给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个连续子序列，使其和最大，输出最大子序列的和。
# 例如，对于L=[2,-3,3,50]， 输出53（分析：很明显，该列表最大连续子序列为[3,50]).
L = [2, -3, 3, 50]
max = L[0]
for i in range(len(L)):
    for j in range(i+1,len(L)+1):
        result = sum(L[i:j])
        if result>max:
            max = result
print(max);