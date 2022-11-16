# 定义变量
age = int(input("多大了？\n"))
# 进行判断
if age >= 18:
    print("我已经成年了")
else:
    print("小朋友")


mesgs = """
尊敬的用户：VIP用户可享受蓝光画质，SVIP用户可在VIP基础上额外享受免广告服务
请输入您要充值的类型：
1：vip用户
2：svip用户
"""
print(mesgs)
mone = input('序号：\n')
if "1" == mone:
    print("vip")
elif "2" == mone:
    print("svip")
else:
    print("无效")


import random

num = random.randint(1, 10)
guess_num = int(input("输入你要猜测的数字："))

if guess_num == num:
    print("恭喜，第一次就猜中了！")
else:
    if guess_num > num:
        print("你猜测的数字大了~")
    else:
        print("你猜测的数字小了~")
    guess_num = int(input("再次输入你要猜测的数字："))

    if guess_num == num:
        print("恭喜，第二次猜中了！")
    else:
        if guess_num > num:
            print("你猜测的数字大了~")
        else:
            print("你猜测的数字小了~")
        guess_num = int(input("第三次输入你要猜测的数字："))

        if guess_num == num:
            print("第三次猜中了！")
        else:
            print("三次机会用完了，没有猜中~~~")
