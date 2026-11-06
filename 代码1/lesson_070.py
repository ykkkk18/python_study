# 配套重写示例，非课程源码逐行转录。
from collections import Counter
def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))
print("素数:", [n for n in range(2, 21) if is_prime(n)])
print("词频:", dict(Counter("python python code".split())))
