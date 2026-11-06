# 配套重写示例，非课程源码逐行转录。
class StudyList:
    def __init__(self, items):
        self.items = list(items)
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return "、".join(self.items)
    def __getitem__(self, index):
        return self.items[index]
s = StudyList(["函数", "文件"])
print(len(s), str(s), s[0])
