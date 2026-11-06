# 配套重写示例，非课程源码逐行转录。
names = ["甲", "乙", "丙"]
scores = [80, 90, 70]
print(dict(zip(names, scores)))
print(list(enumerate(names, start=1)))
print(sum(scores), max(scores), min(scores), all(x >= 60 for x in scores))
