# 弦截法
import math
import sys


def f(xe):
    ye = xe * (math.e ** xe) - 1
    return ye


x0 = 0.5  # 初始值1
x1 = 0.6  # 初始值2
e = 0.000001  # 误差要求
N = 1000  # 最大迭代次数
k = 0  # 迭代次数计数

while k < N:
    x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    if abs(f(x2)) < e:
        print("方程的解为:%f" % x2)
        sys.exit()
    else:
        k = k + 1
        x0 = x1
        x1 = x2

print("计算失败")
