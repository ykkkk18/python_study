# 配套重写示例，非课程源码逐行转录。
def multiplier(factor):
    def apply(value):
        return value * factor
    return apply
double = multiplier(2)
print(double(5))
