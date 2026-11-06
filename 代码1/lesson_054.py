# 配套重写示例，非课程源码逐行转录。
import re
text = "<b>甲</b><b>乙</b>"
print(re.findall(r"<b>.*</b>", text))
print(re.findall(r"<b>.*?</b>", text))
print(re.sub(r"\d+", "#", "订单123已完成"))
