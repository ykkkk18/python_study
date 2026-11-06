# 配套重写示例，非课程源码逐行转录。
def squares(limit):
    for n in range(limit):
        yield n * n
g = squares(4)
print(next(g))
print(list(g))
print(sum(n * n for n in range(4)))
