# 配套重写示例，非课程源码逐行转录。
values = [10, 20]
iterator = iter(values)
print(next(iterator), next(iterator))
print(next(iterator, "已结束"))
print(list(values), list(iterator))
