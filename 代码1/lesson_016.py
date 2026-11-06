# 配套重写示例，非课程源码逐行转录。
scores = {"小林": 90, "小周": 85}
print(list(scores.items()))
print(scores.get("新同学", 0))
a, b = {1, 2, 3}, {3, 4}
print(sorted(a & b), sorted(a | b), sorted(a - b))
