import random

count = 0
num = random.randint(1, 100)
flag = True

while flag:
    guess_num = int(input("请输入你猜的数字："))
    count += 1
    if guess_num == num:
        print("你猜对了，恭喜恭喜！！！答案是{}".format(num))
        flag = False
    else:
        if guess_num >= num:
            print("你猜大了~~~")
        else:
            print("你猜小了~~~")

print("你一共猜了{}次~~~".format(count))

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t", end='')
        j += 1
    i += 1
    print()