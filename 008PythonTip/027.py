# 一个环形的公路上有n个加油站，编号为0,1,2,...n-1,
# 每个加油站加油都有一个上限，保存在列表limit中，即limit[i]为第i个加油站加油的上限，
# 而从第i个加油站开车开到第(i+1)%n个加油站需要cost[i]升油,cost为一个列表。
# 现在有一辆开始时没有油的车，要从一个加油站出发绕这个公路跑一圈回到起点。
# 给你整数n，列表limit和列表cost,你来判断能否完成任务。
# 如果能够完成任务，输出起始的加油站编号，如果有多个,输出编号最小的。
# 如果不能完成任务，输出=-1。
# 加油站，0到n-1
# 加油上限，limit[i]

limit = [2, 4, 6]
cost = [3, 5, 3]
n = 3
res = []
for i in range(n):  # 任意一个点出发
    oil_in_car = limit[i]
    for j in range(n):
        if oil_in_car < cost[(i + j) % n]:  # 判断到下一个点车内的油是否够
            oil_in_car = -1  # 便于下面判断oil_in_car >= 0，没有赋值的话就会把错误结果加入res
            break
        else:
            oil_in_car += limit[(i + j+1) % n] - cost[(i + j) % n]  # 从i+j到i+j+1经加过油后再赋值，还好题目有%n，不然可能会遗漏
    if oil_in_car >= 0:
        res.append(i)

if len(res) == 0:
    print(-1)
else:
    print(min(res))
