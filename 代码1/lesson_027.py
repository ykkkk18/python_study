# 配套重写示例，非课程源码逐行转录。
from functools import wraps
def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("调用:", func.__name__)
        return func(*args, **kwargs)
    return wrapper
@trace
def add(a, b):
    return a + b
print(add(2, 3))
print(add.__name__)
