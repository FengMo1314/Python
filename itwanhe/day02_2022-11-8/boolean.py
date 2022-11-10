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
num: int = 20
sum: int = 0
fn: int = input('请输入第一次猜想的数字\t')
if fn > num:
    sum += 1
    n = input("大了:\t")
    if n > num:
       s = input('大了:\t')
    elif n < num:
        print("小了")
elif fn < num:
    print("小了")
    sum += 1
if sum <= 3:
    if fn == num:
        print("猜对了")
else:
    print("次数用完了")
