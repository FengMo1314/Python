# 定义字符串name
name = "itheima"
# for循环处理字符串
for x in name:
    print(x)

name1 = "itheima is a brand of itcast"
count = 0

for x in name1:
    if x == "a":
        count += 1

print(f"{name1}中被统计的字符串中有{count}个a")

# for循环处理字符串
for i in range(5):
    print(i)

for i in range(1, 10):
    for j in range(1, i + 1):
        # print(f"{j} * {i} = {j * i}\t", end='')
        print("{} * {} = {}\t".format(i, j, i * j), end='')
    print()

money = 10000

for i in range(1, 21):
    import random
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}，绩效分{score}，低于5，不发工资，下一位。")
        continue
    else:
        money -= 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{money}元")
        if money == 0:
            print("工资发完了，下个月领取吧。")
            break
