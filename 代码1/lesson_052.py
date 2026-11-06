# 配套重写示例，非课程源码逐行转录。
import re
for text in ["123456", "123", "abc123"]:
    print(text, bool(re.fullmatch(r"\d{6}", text)))
print(re.findall(r"a+", "baaacaa"))
