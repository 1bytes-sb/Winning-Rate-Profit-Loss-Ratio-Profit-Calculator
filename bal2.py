import random
import statistics  # 用于计算中位数

def modify_value(value):
    """50% 的概率乘以 0.9，50% 的概率乘以 1.1"""
    if random.random() < 0.5:
        return value * 0.6
    else:
        return value * 1.6

# 初始值
original_value = 100
greater_count = 0  # 记录最终值大于初始值的次数
num_experiments = 1000  # 运行的总次数
final_values = []  # 用于记录每次运行的最终值

for experiment in range(num_experiments):
    current_value = original_value
    for _ in range(1000):  # 每次运行的修改循环
        current_value = modify_value(current_value)
    
    # 保存最终值
    final_values.append(current_value)

    # 检查最终值是否大于初始值
    if current_value > original_value:
        greater_count += 1

    print(f"第 {experiment + 1} 次运行的最终值: {current_value}")

# 计算统计数据
average_value = sum(final_values) / len(final_values)
max_value = max(final_values)
min_value = min(final_values)
median_value = statistics.median(final_values)

# 输出统计结果
print(f"\n共有 {greater_count} 次最终值大于初始值 ({num_experiments} 次运行)。")
print(f"所有最终值的平均数: {average_value}")
print(f"所有最终值的最大值: {max_value}")
print(f"所有最终值的最小值: {min_value}")
print(f"所有最终值的中位数: {median_value}")
