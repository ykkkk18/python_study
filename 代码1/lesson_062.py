# 配套重写示例，非课程源码逐行转录。
import random
rng = random.Random(42)
print(rng.randint(1, 10))
print(rng.sample(["变量", "循环", "函数", "文件"], 2))
# 固定种子便于复现实验，不用于安全令牌。
