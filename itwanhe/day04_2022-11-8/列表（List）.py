# from os import remove
# 列表
list = [1, 3, 5, 7, 9, 9, "9"]
# 嵌套
list1 = [[0, 1, 2], [3, 4, 5, 6], [7, 8, 9]]
print(list1[1][3])
# 查询元素索引index
indexs_1 = list.index(9)
indexs_2 = list.index("9")
print(indexs_1, indexs_2)
# 插入——
# 可指定任意位置
list.insert(0, "star")
print(list)
# 追加——尾部
list.append("end")
print(list)
# 删除——del
del list[1]
print(list)
# 删除——remove
list.remove("9")  # 按照内容删除
list.remove(list[1])  # 按照下标删除
print(list)
# 删除——
pop = list.pop(1)
print(f"删除的是{pop}——剩余列表内容为")
print(list)
