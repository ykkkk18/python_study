# 配套重写示例，非课程源码逐行转录。
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b
print("斐波那契:", list(fibonacci(8)))
rows = [{"name": "甲", "score": 80}, {"name": "乙", "score": 95}]
print("最高分:", max(rows, key=lambda row: row["score"]))
