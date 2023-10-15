import numpy as np
from scipy.optimize import minimize_scalar
def target_function(x):
    return x**2 - 4*x + 4  # 例如，这里是一个一元二次函数
# 定义区间
start = 0
end = 5

# 找到最小值
result_min = minimize_scalar(target_function, bounds=(start, end), method='bounded')

# 找到最大值
result_max = minimize_scalar(lambda x: -target_function(x), bounds=(start, end), method='bounded')

if result_min.success and result_max.success:
    print(f"在区间 [{start}, {end}] 内的最小值是 {result_min.fun}，达到最小值的位置是 {result_min.x}")
    print(f"在区间 [{start}, {end}] 内的最大值是 {result_max.fun}，达到最大值的位置是 {result_max.x}")
else:
    print("未能找到最值")


