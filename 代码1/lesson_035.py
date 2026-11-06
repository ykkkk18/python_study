# 配套重写示例，非课程源码逐行转录。
class Settings:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
print(Settings() is Settings())
# 仅展示最小单例；并发初始化还需要额外设计。
