# 配套重写示例，非课程源码逐行转录。
class Animal:
    def speak(self):
        return "声音"
class Dog(Animal):
    def speak(self):
        return super().speak() + ": 汪"
print(Dog().speak())
