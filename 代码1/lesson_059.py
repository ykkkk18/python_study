# 配套重写示例，非课程源码逐行转录。
import time
value = time.strptime("2026-11-06", "%Y-%m-%d")
print(time.strftime("%Y/%m/%d", value))
print("月份:", value.tm_mon)
