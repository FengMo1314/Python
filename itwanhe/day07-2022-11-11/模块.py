# 导入时间模块
import time

print("开始")
# 让程序睡眠1秒(阻塞)
time.sleep(1)
print("结束")
# 导入时间模块中的sleep方法
from time import sleep

print("开始")
# 让程序睡眠1秒(阻塞)
sleep(1)
print("结束")
# 导入时间模块中所有的方法
from time import *

print("开始")
# 让程序睡眠1秒(阻塞)
sleep(1)
print("结束")
# 模块别名
import time as tt
tt.sleep(2)
print('hello')
# 功能别名
from time import sleep as sl
sl(2)
print('hello')
