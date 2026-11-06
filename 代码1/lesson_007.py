# 配套重写示例，非课程源码逐行转录。
from unittest.mock import patch
with patch("builtins.input", return_value="7"):
    days = int(input("学习天数："))
print("每天分钟:", 1470 // days, "余数:", 1470 % days)
print("第一行\n第二行")
