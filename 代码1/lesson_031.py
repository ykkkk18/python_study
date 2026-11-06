# 配套重写示例，非课程源码逐行转录。
class Account:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("金额必须为正")
        self.__balance += amount
    @property
    def balance(self):
        return self.__balance
a = Account()
a.deposit(100)
print(a.balance)
# __del__ 的运行时机不适合承担关键文件关闭；使用 with。
