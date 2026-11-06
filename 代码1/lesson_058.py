# 配套重写示例，非课程源码逐行转录。
import time
timestamp = 0
value = time.gmtime(timestamp)
print("UTC年:", value.tm_year)
print(time.strftime("%Y-%m-%d %H:%M:%S", value))
