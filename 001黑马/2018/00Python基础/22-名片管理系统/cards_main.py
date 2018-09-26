import cards_input
import cards_tools

print("*" * 30)
print("欢迎使用【名片管理系统】V1.0")
print("1：新建名片")
print("2：显示全部")
print("3：查询名片")
print("0：退出系统")
print("*" * 30)
action_str = input("请选择需要执行的操作:")
print("您选择的操作是『%s』" % action_str)
if action_str in ["1","2","3"]:
    pass
elif action_str =="0":
    pass
else:
    print("您输入的条件不正确，请重新选择")