import numpy as np
import matplotlib.pyplot as plt

# ===================== 1. 原始数据 =====================
# 假设这是10个模型的准确率（0~1之间）
accuracy = np.array([0.92, 0.88, 0.95, 0.91, 0.87, 
                     0.93, 0.89, 0.94, 0.90, 0.86])

print(f"原始数据: {accuracy}")
print(f"原始均值: {np.mean(accuracy):.4f}\n")

# ===================== 2. Bootstrap抽样 =====================
n_iterations = 100000   # 重复抽样次数
n_samples = len(accuracy)  # 每次抽样的样本量（与原数据集相同）
bootstrap_means = []   # 存储每次抽样的均值

for i in range(n_iterations):
    # 从原始数据中有放回地抽取 n_samples 个样本
    bootstrap_sample = np.random.choice(accuracy, size=n_samples, replace=True)
    # 计算这个自助样本的均值
    bootstrap_means.append(np.mean(bootstrap_sample))

# 转换为numpy数组方便计算
bootstrap_means = np.array(bootstrap_means)

# ===================== 3. 计算置信区间 =====================
# 方法一：百分位数法（推荐，不依赖分布假设）
ci_lower = np.percentile(bootstrap_means, 2.5)   # 2.5%分位数
ci_upper = np.percentile(bootstrap_means, 97.5)  # 97.5%分位数

print(f"Bootstrap均值的均值: {np.mean(bootstrap_means):.4f}")
print(f"95%置信区间: [{ci_lower:.4f}, {ci_upper:.4f}]")

# 方法二：正态近似法（假设抽样分布近似正态）
ci_mean = np.mean(bootstrap_means)
ci_std = np.std(bootstrap_means)
ci_lower_norm = ci_mean - 1.96 * ci_std
ci_upper_norm = ci_mean + 1.96 * ci_std
print(f"正态近似法 95% CI: [{ci_lower_norm:.4f}, {ci_upper_norm:.4f}]")

# ===================== 4. 可视化结果 =====================
plt.figure(figsize=(10, 5))

# 绘制Bootstrap均值的分布直方图
plt.subplot(1, 2, 1)
plt.hist(bootstrap_means, bins=50, edgecolor='black', alpha=0.7, color='skyblue')
plt.axvline(ci_lower, color='red', linestyle='--', label=f'2.5%: {ci_lower:.4f}')
plt.axvline(ci_upper, color='red', linestyle='--', label=f'97.5%: {ci_upper:.4f}')
plt.axvline(np.mean(accuracy), color='green', linestyle='-', linewidth=2, label=f'Original Mean: {np.mean(accuracy):.4f}')
plt.xlabel('Bootstrap AVG')
plt.ylabel('Frequency')
plt.title('Bootstrap Sampling Distribution')
plt.legend()

# 绘制箱线图看分布
plt.subplot(1, 2, 2)
plt.boxplot(bootstrap_means, vert=True)
plt.ylabel('Bootstrap AVG')
plt.title('Bootstrap AVG Boxplot')
plt.xticks([1], [''])

plt.tight_layout()
plt.show()