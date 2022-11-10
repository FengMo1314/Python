# 单行注释


print("Hello World!")
"""
多行注释——不推荐使用
"""
print("""
多行
字符
串
""")
a = "123"
print(a)
# 字符串转换为基础类型——转化内容必须有效
print(int(a))
# list列表
list1 = [1, 3, 2, 4, 6]
print("列表第2个", list1[1])
# 元组
zu = (1, 2, 3, 4)
print("元组第1个", zu[0])
# 字典
doc = {"key1": "val1", "key2": "val2"}
print("字典建为key2的", doc["key2"])
print("*" * 10 + "运算" + "*" * 10)
int1 = 10
int2 = 3
double1 = 3.00
print("10/3.00=", int1 / double1)
double2 = 2.11
double3 = 1.11
print("2.11/1.11=", double2 / double3)
print("//——取整除:10//3=", int1 // int2)
print("**——幂：2^3=", 2 ** 3)
print("精确解决除不尽精度问题：round(10/3)——默认不保留", round(10 / 3))
print("精确解决除不尽精度问题：round(10/3,2)——保留2位", round(10 / 3, 2))
print("*" * 10 + "赋值运算符" + "*" * 10)
val1 = 10
val2 = 3.0
val1 /= val2
print("val1=val1/val2=", val1)
val2 *= val1
print("val2=val1*val2=", val2)

print("*" * 10 + "字符引用" + "*" * 10)
String = "''"
print("双引号包含:''=", String)
String = " \"\" "
print("转义字符\"\"=", String)
String2 = "万和"
print("学it来:%s ,%s" % (String2, String))
clazz = "软件211"
year = 2024
money = 9999.50
message = "常州信息职业技术学院的%s,将于%i年毕业,预计薪资为%0.2f" % (clazz, year, money)
print("字符串格式化（采用从c的）%s" % message)
name = "万和"
stock_price = 299
stock_code = 222
stock_price_d_g_f = 2.1
growth_days = 5
message = f"""{name}公司,
股价{stock_price}*系数{stock_price_d_g_f}**{growth_days}天=
{round(stock_price * stock_price_d_g_f ** growth_days, 2)}元 """
print(message)
# input——输入
message = {"class": input("输入班级:\n"), "name": input("姓名:\n")}
print(f"welcome{message['class']}的{message['name']}")
