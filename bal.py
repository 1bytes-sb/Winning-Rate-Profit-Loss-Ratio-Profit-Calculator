import random

def modify_value(value):
    """50% 的概率乘以 0.9，50% 的概率乘以 1.1"""
    if random.random() < 0.49:
        return value * 0.91
    else:
        return value * 1.11

# 初始值
original_value = 100

# 循环修改 10 次
current_value = original_value
print(f"初始值: {current_value}")

for i in range(1, 100):  # 循环 10 次
    current_value = modify_value(current_value)
    print(f"第 {i} 次修改后的值: {current_value}")
