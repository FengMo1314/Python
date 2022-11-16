# while
sum = 0
while True:
    if sum == 1000:
        break
    print(f"ss{sum}")
    sum += 1
cont = 1
sum1 = 0
while cont <= 100:
    sum1 = sum1 + cont
    cont += 1
print(sum1)
# for
for i in (1, 2, 3, 4, 7):
    print(i)
# range
num = int(input("输入偶数最大区间:\t"))
cont1 = 0
for i in range(0, num + 1, 2):
    # print(i)
    if i != 0:
        cont1 += 1
print(cont1)

sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print('1-100累加的和是：{}'.format(sum))