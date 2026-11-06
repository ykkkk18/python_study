# 配套重写示例，非课程源码逐行转录。
from greenlet import greenlet
def first():
    print("A1")
    g2.switch()
    print("A2")
def second():
    print("B1")
    g1.switch()
g1 = greenlet(first)
g2 = greenlet(second)
g1.switch()
