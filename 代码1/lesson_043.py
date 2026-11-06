# 配套重写示例，非课程源码逐行转录。
from concurrent.futures import ThreadPoolExecutor
def square(n):
    return n * n
with ThreadPoolExecutor(max_workers=2) as pool:
    print(list(pool.map(square, [1, 2, 3])))
