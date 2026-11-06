# 配套重写示例，非课程源码逐行转录。
from functools import wraps
def tag(name):
    def decorate(func):
        @wraps(func)
        def wrapper():
            print(name, "进入")
            result = func()
            print(name, "离开")
            return result
        return wrapper
    return decorate
@tag("外层")
@tag("内层")
def work():
    print("工作")
work()
