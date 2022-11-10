import random

# 判断结构
num = random.randint(1, 10)
snum = int(input("输入：\t"))
if snum > num:
    snum = int(input("大了：\t"))
    if snum > num:
        snum = int(input("大了：\t"))
        if snum != num:
            print("次数用完了")
        else:
            print("猜对了")
    elif snum < num:
        snum: int = int(input("小了：\t"))
        if snum != num:
            print("次数用完了")
        else:
            print("猜对了")
    else:
        print("猜对了")
elif snum < num:
    snum: int = int(input("小了：\t"))
    if snum > num:
        snum: int = int(input("大了：\t"))
        if snum != num:
            print("次数用完了")
        else:
            print("猜对了")
    elif snum < num:
        snum: int = int(input("小了：\t"))
        if snum != num:
            print("次数用完了")
        else:
            print("猜对了")
    else:
        print("猜对了")
else:
    print("猜对了")
# 循环结构
num2 = random.randint(1, 10)
falg = True
snum2 = int(input("首次输入数字：\t"))
sum = 1
while falg:
    if snum2 < num2:
        snum2 = int(input(f"小了——猜了{sum}次:\t"))
        sum += 1
    elif snum2 > num2:
        snum2 = int(input(f"大了——猜了{sum}次:\t"))
        sum += 1
    else:
        print(f"恭喜猜对了——猜了{sum}次")
        falg = False
