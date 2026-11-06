# 配套重写示例，非课程源码逐行转录。
import re
text = "A1 中2"
print(re.findall(r"\d", text))
print(re.findall(r"[A-Z]", text))
print(re.findall(r"\s", text))
