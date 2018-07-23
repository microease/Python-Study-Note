# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
year = int(input("请输入年份：\n"))
month = int(input("请输入月份：\n"))
day = int(input("请输入天：\n"))
months1 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]  # 闰年
months2 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]  # 平年
result = 0
if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 100 == 0) and (year % 400 == 0)):
    result = months1[month - 1] + day
else:
    result = months2[month - 1] + day
print("是该年的第%d天" % result)
