# 元组——不可增加，删除，修改
tuple = (1)  # int
print(type(tuple))
tuple1 = (1, 2, "3")  # tuple
print(type(tuple1))
# 查询元组
s = tuple1[2]
print(f"元组下标为2的是{s},其类型为：{type(s)}")
# 嵌套式的元组只可对其内部的其他容器内容进行修改
tuple2 = (1, 2, [3, 4, 5, 6])
tuple2_list = tuple2[2]
tuple2_list.remove(6)
print(tuple2,"\n",len(tuple2))

