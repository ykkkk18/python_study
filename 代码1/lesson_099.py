# 配套重写示例，非课程源码逐行转录。
from urllib.parse import urlsplit
proxy = "http://127.0.0.1:8080"
print("代理协议:", urlsplit(proxy).scheme)
print("代理地址:", urlsplit(proxy).hostname)
print("仅解释配置，未连接代理")
