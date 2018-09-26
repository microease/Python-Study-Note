card_list = []


def show_menus():
    """显示菜单"""
    print("*" * 30)
    print("欢迎使用【名片管理系统】V1.0")
    print("1：新建名片")
    print("2：显示全部")
    print("3：查询名片")
    print("0：退出系统")
    print("*" * 30)


def new_card():
    """新增名片"""
    print("-" * 30)
    print("新增名片")
    # 1：提示用户输入名片的详细信息
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ：")
    email = input("请输入邮箱：")
    # 2：使用用户输入的名片信息建立字典
    card_dict = {"name": name, "phone": phone, "qq": qq, "email": email}
    # 3：将名片字典添加到列表中
    card_list.append(card_dict)
    # 4：提示用户添加成功
    print("添加%s的名片成功！" % name)


def show_all():
    """显示所有名片"""
    print("-" * 30)
    print("显示所有名片")


def search_card():
    """搜索名片"""
    print("-" * 30)
    print("搜索名片")
