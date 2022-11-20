# 位置参数
def where(name, age):
    print(f"name:{name},age:{age}")


where("柳和", 22)


# 关键参数
def imp(name, age, ids):
    print(f"id:{ids},其他{name, age}")


imp("柳和", 20, ids=123)


# 缺省参数

def non(name, age, day):
    print(f"name{name}\nage{age}\nday{day}")


non("柳和", 20, "2022-11-9")


# 不定长参数
def many(*mes):
    print(mes)


many("柳和", 20)
many(20, 2022, "11-9")


# 关键字传递
def impot(**mes):
    print(mes)


impot(name="柳和", age=20, day="2022")


# 匿名函数
def fun(com):
    result = com(12, 4)
    print("匿名函数",result)


fun(lambda x, y: x * y)
