# 配套重写示例，非课程源码逐行转录。
class A:
    def name(self):
        return "A"
class B(A):
    pass
class C(A):
    def name(self):
        return "C"
class D(B, C):
    pass
print([cls.__name__ for cls in D.__mro__])
print(D().name())
