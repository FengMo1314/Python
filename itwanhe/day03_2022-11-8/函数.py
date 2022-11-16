def f():
    print("这是一个函数")


f()

money: float = 5000000


def mes(user: str, s: str):
    while True:
        msg = int(input(f"""
{s * 10}主菜单{s * 10}
    {user},您好，欢迎使用本行ATM，请选择操作
    查询余额[输入1]
    存款[输入2]
    取款[输入3]
    退出[输入4]
    请输入您的选择：\t
"""))
        if msg == 1:
            cha(user, s)
        elif msg == 2:
            sav_money = float(input("存款金额：\t"))
            cun(user, sav_money)
        elif msg == 3:
            qu_money = float(input("取款金额：\t"))
            qu(user, qu_money)
        elif msg == 4:
            break
        else:
            print(f"输入非法，请重输")


def cha(user: str, s: str):
    print(f"{s * 10}查询结果{s * 10}")
    yu(user, 1, 0)


def yu(user: str, typ: int, mone: float):
    global money  # 引用全局变量
    if typ == 2:
        money += mone
    elif typ == 3:
        if mone <= money:
            money -= mone
    print(f"""{user}，您好，您的余额剩余{round(money, 2)} """)


def cun(user: str, mone: float):
    # global money  # 引用全局变量
    if mone >= 0.01:
        print(f"{user}，您好，您存款{mone}元成功")
        yu(user, 2, mone)
    else:
        print("最低金额0.01元")


def qu(user: str, mone: float):
    # global money  # 引用全局变量
    if mone > money:
        print(f"{user}，您好，您取款{mone}元失败——余额不足")
    else:
        print(f"{user}，您好，您取款{mone}元成功")
    yu(user, 3, mone)


mes("柳和", "***")
